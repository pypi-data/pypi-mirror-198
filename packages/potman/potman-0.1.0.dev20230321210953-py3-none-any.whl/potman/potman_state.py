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


import pathlib

import anyjsonthing

import potman.config as cfg

from typing import Final
from typing import Optional


class PotmanState(object):
    """TODO: docs

    Attributes:
        config: TODO
        data_dir: TODO
        potman_dir: TODO
    """

    _CONFIG_FILE_NAME: Final[str] = "potman-config.json"
    """The name of the config file that is stored in the potman directory."""

    _DATA_DIR_NAME: Final[str] = "data"
    """The name of the sub-directory of the potman directory that cloned feature repos are placed in."""

    _DEFAULT_POTMAN_DIR: Final[pathlib.Path] = pathlib.Path.home() / ".potman"
    """The path of the default potman-directory."""

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, config: cfg.PotmanConfig, potman_dir: pathlib.Path) -> None:
        """Creates a new :class:`~.PotmanState`."""

        self._config = config
        self._potman_dir = potman_dir

        self._data_dir = self._potman_dir / self._DATA_DIR_NAME

    #  PROPERTIES  #####################################################################################################

    @property
    def config(self) -> cfg.PotmanConfig:

        return self._config

    @property
    def data_dir(self) -> pathlib.Path:

        return self._data_dir

    @property
    def potman_dir(self) -> pathlib.Path:

        return self._potman_dir

    #  METHODS  ########################################################################################################

    @classmethod
    def _initialize(cls, potman_dir: pathlib.Path) -> None:
        """Initializes the specified ``potman_dir``.

        To that end, the directory is created, if it does not exist yet, and a default config file is generated.

        Args:
            potman_dir: The path of the directory that is initialized as potman directory.

        Raises:
            ValueError: If the ``potman_dir`` already contains a config file.
        """

        # First, we check if the potman_dir has been initialized already (which is the case if it contains a config
        # file).
        config_path = potman_dir / cls._CONFIG_FILE_NAME
        if config_path.is_file():

            raise ValueError("The specified <potman_dir> is initialized already")

        # Next, we create the directory (if it does not exist yet) and generate a default config.
        potman_dir.mkdir(parents=True, exist_ok=True)
        anyjsonthing.IO.dump(cfg.PotmanConfig(), config_path)

    @classmethod
    def create(cls, potman_dir: pathlib.Path = _DEFAULT_POTMAN_DIR) -> "PotmanState":
        """Creates a new instance of :class:`~.PotmanState` that uses the provided ``potman_path``.

        If the specified ``potman_dir`` does not exist or does not contain a config file, then it is automatically
        initialized as a new potman directory.

        Args:
            potman_dir: The :attr:`~.potman_dir` used by the created instance.

        Returns:
            The created :class:`~.PotmanState`.
        """

        # First, we check if the potman_dir has been initialized already, and initialize it, if not.
        config_path = potman_dir / cls._CONFIG_FILE_NAME
        if not config_path.is_file():

            cls._initialize(potman_dir)

        # Next we load the config file from the disk and create a new PotmanState.
        config = anyjsonthing.IO.load(cfg.PotmanConfig, config_path)
        return cls(config, potman_dir)

    def dump_config(self, update_last_updated: bool = False) -> None:
        """Persists the stored :attr:`~.config` in the used :attr:`~.potman_dir`.

        Args:
            update_last_updated: If ``True``, then the :attr:`~.cfg.PotmanConfig.last_updated` attribute of the stored
                :attr:`~.config` is updated to "now".
        """

        if update_last_updated:

            self._config.update_last_updated()

        config_path = self._potman_dir / self._CONFIG_FILE_NAME
        anyjsonthing.IO.dump(self._config, config_path)

    def get_feature_store_config_by_id(self, feature_store_id: str) -> Optional[cfg.FeatureStoreConfig]:
        """Retrieves the :class:`~.cfg.FeatureStoreConfig` of the feature store with the given ``feature_store_id``.

        If there is no feature store with the given ID, then ``None`` is retrieved instead.

        Args:
            feature_store_id: The ID of the feature store that the :class:`~.cfg.FeatureStoreConfig` is requested of.

        Returns:
            The requested :class:`~.cfg.FeatureStoreConfig` or ``None`` if the ``feature_store_id`` is unknown.
        """

        for feature_store_config in self._config.feature_stores:

            if feature_store_config.id == feature_store_id:

                return feature_store_config

    def get_feature_store_configs_by_project_name(self, project_name: str) -> list[cfg.FeatureStoreConfig]:
        """Retrieves the :class:`~.cfg.FeatureStoreConfig`\ s of all feature store with the given ``project_name``.

        Args:
            project_name: The project name of the feature stores that the :class:`~.cfg.FeatureStoreConfig`\ s are
                requested of.

        Returns:
            The requested :class:`~.cfg.FeatureStoreConfig`\ s.
        """

        return [x for x in self._config.feature_stores if x.project_name == project_name]

    def get_feature_store_dir_by_id(self, feature_store_id: str) -> pathlib.Path:
        """Retrieves the :class:`~pathlib.Path` that the feature store with the given ID is cloned into.

        Note:
            The retrieved :class:`~pathlib.Path` may refer to a directory that does not exist yet, if the feature store
            has not been cloned yet.

        Args:
            feature_store_id: The ID of the feature store that the clone-directory is retrieved of.

        Returns:
            The :class`~pathlib.Path` of the directory that the feature store with the specified ``feature_store_id`` is
            cloned into.
        """

        return self.data_dir / feature_store_id
