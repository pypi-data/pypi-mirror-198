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


"""A library the provides easy access to data stored in a Feast feature store."""


import os
import re

import feast
import feast.infra.offline_stores.file as file
import pandas as pd

import potman.potman_state as potman_state
import potman.toolkit as toolkit

from typing import Final


_DATASET_REGEX: Final[re.Pattern] = re.compile("^(?P<project>[A-Za-z0-9_-]+):(?P<feature_service>[A-Za-z0-9_-]+)$")
"""A regex for parsing dataset identifiers."""


def fetch(dataset: str) -> pd.DataFrame:
    """TODO: docs

    Args:
        dataset: The identifier of the dataset to fetch.

    Returns:
        A :class:`~pd.DataFrame` that contains the requested dataset.

    Raises:
        ValueError: If the provided ``dataset`` is not a valid identifier of a dataset or if it was mapped to either
            none or more than one dataset.
    """

    # To start with, we parse the provided name of the dataset to fetch into its constituents.
    match = re.match(_DATASET_REGEX, dataset)
    if not match:

        raise ValueError(f"Invalid <dataset> name: <{dataset}>")

    project_name, feature_service_name = dataset.split(":")

    # Next, we create the Potman state and toolkit to use.
    state = potman_state.PotmanState.create()
    tk = toolkit.Toolkit(state)

    # We fetch the configurations of all projects that match the requested project name.
    project_configs = state.get_feature_store_configs_by_project_name(project_name)

    if len(project_configs) == 1:

        # If we found exactly one project with the requested project name, then we perform a pull for that specific
        # project to ensure that it is up-to-date.
        tk.pull_feature_store_by_id(project_configs[0].id)

    else:  # -> len(project_configs) != 1

        # If no/multiple projects were found for the given project_name, then we perform a pull for all projects to
        # ensure that the absence/ambiguity of the required project name is not due to stale data.
        tk.pull_all_feature_stores()

    # Once again, we fetch the configurations of all projects that match the requested project name. At this point, we
    # can only continue if there is exactly one.
    project_configs = state.get_feature_store_configs_by_project_name(project_name)
    if len(project_configs) != 1:

        raise ValueError(f"Found {len(project_configs)} for project name <{project_name}>")

    project_config = project_configs[0]

    # If the project requires profile-based AWS authentication, then we update the respect environment variable
    # accordingly.
    if project_config.aws_profile is not None:

        os.environ["AWS_PROFILE"] = project_config.aws_profile

    # Now we are ready to create an instance representing the Feast feature store specified by the considered project.
    project_dir = state.get_feature_store_dir_by_id(project_config.id)
    store = feast.FeatureStore(repo_path=str(project_dir.absolute()))
    offline_store = file.FileOfflineStore()

    # A slightly annoying aspect of retrieving data from Feast is that it requires us to provide an entity data-frame
    # for so-called point-in-time joins. (Please look at the Feast documentation for additional information.) To create
    # such a data frame, we simply read the first (i.e., index 0) feature view contained in the considered feature
    # service as is, keep only the join columns plus event stamp, and update the event timestamp to "now".
    feature_service = store.get_feature_service(feature_service_name)
    feature_0 = store.get_feature_view(feature_service.feature_view_projections[0].name)
    entity_df = offline_store.pull_latest_from_table_or_query(
            config=store.config,
            data_source=store.get_data_source(feature_0.batch_source.name),
            join_key_columns=feature_0.join_keys,
            feature_name_columns=feature_0.join_keys,
            timestamp_field="event_timestamp",
            created_timestamp_column=None,
            start_date=pd.to_datetime("2000-01-01 00:00:00.000", utc=True),
            end_date=pd.to_datetime("now", utc=True)
    ).to_df()
    entity_df["event_timestamp"] = pd.to_datetime("now", utc=True)

    # Finally, we fetch the requested data from Feast using the entity data-frame created above.
    return store.get_historical_features(entity_df, features=feature_service).to_df()
