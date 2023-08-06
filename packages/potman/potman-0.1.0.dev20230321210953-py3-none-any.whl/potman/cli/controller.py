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


import dulwich.errors

import potman.cli.actions as actions
import potman.cli.model as m
import potman.cli.view as v
import potman.cli.view_observer as view_observer
import potman.potman_state as potman_state
import potman.toolkit as toolkit


class Controller(view_observer.ViewObserver):

    #  CONSTRUCTOR  ####################################################################################################

    def __init__(self, model: m.Model, view: v.View) -> None:
        """Creates a new :class:`~.Controller` that uses the provided :class:`~.m.Model` and :class:`~.v.View`."""

        self._model = model
        self._view = view

        self._potman_state = potman_state.PotmanState.create()
        self._toolkit = toolkit.Toolkit(self._potman_state)

        self._view.register_observer(self)

    #  METHODS  ########################################################################################################

    def action_performed(self, action: actions.Action) -> None:

        if isinstance(action, actions.AddFeatureStoreFinishAction):

            self._toolkit.add_feature_store_config(action.feature_store)
            self._view.print_success_message("OK")
            self._view.print_text("Cloning the repository...")

            try:

                self._toolkit.pull_feature_store_by_id(
                        self._potman_state.config.feature_stores[-1].id
                )
                self._view.print_success_message("OK")

            except (dulwich.errors.HangupException, dulwich.errors.NotGitRepository) as error:

                self._view.print_error_message(f"ERROR -- {error}")

        elif isinstance(action, actions.AddFeatureStoreStartAction):

            self._view.run_add_feature_store_workflow()

        elif isinstance(action, actions.ListFeatureStoresAction):

            self._view.display_feature_stores(
                    self._potman_state.config.feature_stores
            )

        elif isinstance(action, actions.PrintConfigAction):

            self._view.print_config(
                    self._potman_state.config
            )

        elif isinstance(action, actions.PrintHelpAction):

            self._view.print_help()

        elif isinstance(action, actions.PrintPotmanDirAction):

            self._view.print_text(
                    str(self._potman_state.potman_dir)
            )

        elif isinstance(action, actions.PullAction):

            self._toolkit.pull_all_feature_stores()
            self._view.print_success_message("OK")

        elif isinstance(action, actions.QuitAction):

            self._view.stop()

        elif isinstance(action, actions.RemoveFeatureStoreAction):

            try:

                self._toolkit.remove_feature_store_config_by_id(action.feature_store_id)
                self._view.print_success_message("OK")

            except ValueError as error:

                self._view.print_error_message(f"ERROR -- {error}")

    def start(self) -> None:
        """Starts the controller (which basically starts the entire CLI application)."""

        self._view.start()
