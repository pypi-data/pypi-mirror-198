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

import potman.config as config
import potman.feature_store_repo as feature_store_repo


class FeatureStoreRepoFactory(object):
    """A factory for creating instances of :class:`~.feature_store_repo.FeatureStoreRepo`.

    Attributes:
        data_dir: The :class:`~pathlib.Path` of the directory that all feature stores are cloned into, which is usually
            a subdirectory of the Potman directory.
    """

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, data_dir: pathlib.Path) -> None:
        """Creates a new instance of :class:`~.FeatureStoreRepoFactory`."""

        self._data_dir = data_dir

    #  PROPERTIES  #####################################################################################################

    @property
    def data_dir(self) -> pathlib.Path:

        return self._data_dir

    #  METHODS  ########################################################################################################

    def create_repo(
            self,
            feature_store_config: config.FeatureStoreConfig
    ) -> feature_store_repo.FeatureStoreRepo:
        """Creates a :class:`~.feature_store_repo.FeatureStoreRepo` based on the provided ``feature_store_config``."""

        return feature_store_repo.FeatureStoreRepo(
                feature_store_config.clone_url,
                self._data_dir / feature_store_config.id
        )
