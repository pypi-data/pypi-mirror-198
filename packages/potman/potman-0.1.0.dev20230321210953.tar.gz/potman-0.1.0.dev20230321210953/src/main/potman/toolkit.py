# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                     #
#   Copyright (c) 2023, Patrick Hohenecker                                            #
#                                                                                     #
#   All rights reserved.                                                              #
#                                                                                     #
#   Redistribution and use in source and binary forms, with or without                #
#   modification, are permitted provided that the following conditions are met:       #
#                                                                                     #
#       * Redistributions of source code must retain the above copyright notice,      #
#         this list of conditions and the following disclaimer.                       #
#       * Redistributions in binary form must reproduce the above copyright notice,   #
#         this list of conditions and the following disclaimer in the documentation   #
#         and/or other materials provided with the distribution.                      #
#                                                                                     #
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS               #
#   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT                 #
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR             #
#   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER       #
#   OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,          #
#   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,               #
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR                #
#   PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF            #
#   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING              #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS                #
#   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                      #
#                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import shutil

import potman.config as cfg
import potman.feature_store_repo_factory as feature_store_repo_factory
import potman.potman_state as potman_state


class Toolkit(object):
    """Provides tools for manipulating the current state of Potman."""

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, state: potman_state.PotmanState) -> None:
        """Creates a new :class:`~.Toolkit` that operates based on the provided ``state``."""

        self._state = state
        self._repo_factory = feature_store_repo_factory.FeatureStoreRepoFactory(self._state.data_dir)

    #  METHODS  ########################################################################################################

    def add_feature_store_config(self, feature_store_config: cfg.FeatureStoreConfig) -> None:
        """Adds the given ``feature_store_config`` to the :attr:`~.state`."""

        self._state.config.feature_stores.append(feature_store_config)
        self._state.dump_config(update_last_updated=True)

    def clear_cache(self) -> None:
        """Clears all cloned feature stores.

        To that end, this method simply removes the entire data directory. In addition to this, the
        :attr:`~potman.config.feature_store_config.FeatureStoreConfig.last_pull` attribute is set to ``None`` for all
        feature-stores stored in the :attr:`~.Toolkit.state`.
        """

        # First, we remove the data directory, if it exists.
        if self._state.data_dir.is_dir():

            shutil.rmtree(self._state.data_dir)

        # Next, we set last_pull to None for all features stores that exist in the state. Notice that we do this
        # irrespective of whether the data dir did exist. This way, we cover corner cases such as the user manually
        # deleting the data dir.
        for some_store in self._state.config.feature_stores:

            some_store.last_pull = None

    def create_data_dir(self) -> None:
        """Creates the data directory, if it does not exist yet.

        If the data directory exists already, then this is a no-op.
        """

        self._state.data_dir.mkdir(exist_ok=True)

    def pull_all_feature_stores(self) -> None:
        """Performs a pull of the Git projects of all features stores.

        To that end, this method invokes :meth:`~.pull_feature_store_by_id` for all feature stores that exist in the
        :attr:`~.state`.
        """

        for feature_store_config in self._state.config.feature_stores:

            self.pull_feature_store_by_id(feature_store_config.id)

    def pull_feature_store_by_id(self, feature_store_id: str) -> None:
        """Performs a pull of the Git project of the feature store with the specified ``feature_store_id``.

        If the Git repo containing the feature store does not exist yet, then it is automatically cloned. Furthermore,
        the Potman :attr:`~.state` is updated with the project name found in the update repo. Notice further that (in
        contrast with :meth:`~potman.feature_store_repo.FeatureStoreRepo.get_project_name`) this method **does not**
        raise an error when no project name could be retrieved, but instead updates the same to ``None`` in the
        :attr:`~.state`.

        Args:
            feature_store_id: The ID of the feature store that the pull is performed for.

        Raises:
            ValueError: If the provided ``feature_store_id`` is unknown.
        """

        # We fetch the config of the requested feature store, and raise an error if it does not exist.
        feature_store_config = self._state.get_feature_store_config_by_id(feature_store_id)
        if not feature_store_config:

            raise ValueError(f"Unknown <feature_store_id>: <{feature_store_id}>")

        # Next, we create a feature repo, and either clone it (if it does not exist yet) or pull.
        repo = self._repo_factory.create_repo(feature_store_config)
        if repo.exists():

            repo.pull()

        else:

            repo.root_dir.mkdir(parents=True, exist_ok=True)
            repo.clone()

        # Finally, we update the Potman state.
        project_name = None
        try:

            project_name = repo.get_project_name()

        except ValueError:

            pass  # -> Nothing to do.

        feature_store_config.project_name = project_name
        feature_store_config.update_last_pull()
        self._state.dump_config(update_last_updated=True)

    def remove_feature_store_config_by_id(self, feature_store_id: str) -> None:
        """Removes the feature store with the specified ``feature_store_id`` from the :attr:`~.state`.

        Removing the feature store includes removing it from the Potman configuration as well as deleting any cached
        files that belong to the same.

        Args:
            feature_store_id: The ID of the feature store that is removed.

        Raises:
            ValueError: If no feature store with the specified ``feature_store_id`` exists in the :attr:`~.state`.
        """

        # First, we retrieve the index of the config of the considered feature store in the potman config, and raise an
        # error if it does not exist.
        try:

            feature_store_config_idx = next(
                    idx
                    for idx, x in enumerate(self._state.config.feature_stores)
                    if x.id == feature_store_id
            )

        except StopIteration:

            raise ValueError(f"Unknown <feature_store_id>: <{feature_store_id}>")

        # Next, we remove the feature-store config from the potman config.
        del self._state.config.feature_stores[feature_store_config_idx]
        self._state.dump_config(update_last_updated=True)

        # Finally, remove any data that has been retrieved for the deleted feature store.
        feature_store_dir = self._state.get_feature_store_dir_by_id(feature_store_id)
        if feature_store_dir.is_dir():

            shutil.rmtree(feature_store_dir)
