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


import json
import pathlib
import subprocess

import dulwich.porcelain as porcelain


class FeatureStoreRepo(object):
    """Represents a Git repository that contains a Feast feature store.

    Attributes:
        clone_url: The URL used to clone the :class:`~.FeatureStoreRepo`. Typically, this is something like
            ``"git@..."``.
        root_dir: The path of the directory that the :class:`~.FeatureStoreRepo` is cloned into.
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, clone_url: str, root_dir: pathlib.Path) -> None:
        """Creates a new instance of :class:`~.FeatureStoreRepo`."""

        self._clone_url = clone_url
        self._root_dir = root_dir

    #  PROPERTIES  #####################################################################################################

    @property
    def clone_url(self) -> str:

        return self._clone_url

    @property
    def root_dir(self) -> pathlib.Path:

        return self._root_dir

    #  METHODS  ########################################################################################################

    def clone(self) -> None:
        """Clones the :class:`~.FeatureStoreRepo`.

        Raises:
            ValueError: If the :class:`~.FeatureStoreRepo` already exists on the disk (in the :attr:`~.root_dir`).
        """

        # Ensure that the repo hasn't been cloned already.
        if self.exists():

            raise ValueError("The feature repo has been cloned already")

        # Next, we clone the main branch of the repo.
        porcelain.clone(self._clone_url, target=self._root_dir, branch="main")

    def exists(self) -> bool:
        """Evaluates whether the :class:`~.FeatureStoreRepo` has been cloned already."""

        # As an indicator, we look at the .git directory that has to exist in the root of every Git project.
        git_dir = self._root_dir / ".git"
        return git_dir.is_dir()

    def get_project_name(self) -> str:
        """Retrieves the project name as specified in the Feast config contained in the :class:`~.FeatureStoreRepo`.

        Returns:
            The name of the Feast project.

        Raises:
            ValueError: If invoking Feast to receive the project name failed for some reason.
        """

        try:

            completed_process = subprocess.run(
                    ["feast", "registry-dump"],
                    cwd=self._root_dir,
                    check=True,
                    capture_output=True,
                    text=True
            )
            return json.loads(completed_process.stdout)["project"]

        except subprocess.CalledProcessError:

            raise ValueError(
                    "The project name could not be retrieved - "
                    "are you sure the Git project contains a Feast feature store?"
            )

    def pull(self) -> None:
        """Performs a pull.

        Raises:
            ValueError: If the :class:`~.FeatureStoreRepo` has not been cloned yet.
        """

        if not self.exists():

            raise ValueError("The feature repo has not been cloned yet")

        porcelain.pull(self._root_dir)
