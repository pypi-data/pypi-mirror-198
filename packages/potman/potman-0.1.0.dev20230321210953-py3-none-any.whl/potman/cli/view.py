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


import importlib.resources as resources
import json
import pkg_resources
import re

import anyjsonthing
import tabulate
import termcolor

import potman.cli.actions as actions
import potman.cli.view_observer as view_observer
import potman.cli.workflows as workflows
import potman.config as config

from typing import Final
from typing import Iterable
from typing import Optional


class View(object):
    """TODO: docs"""

    _REMOVE_FEATURE_STORE_REGEX: Final[re.Pattern] = \
            re.compile(r"^\s*remove\s+feature-store\s+(?P<id>[A-Za-z0-9-]+)\s*$")
    """A regex for parsing the remove-feature-store command."""

    _HELP_TEXT: Final[str] = (
            f"{termcolor.colored('DESCRIPTION', attrs=['bold'])}\n"
            f"\n"
            f"    Something bla bla...\n"
            f"\n"
            f"{termcolor.colored('COMMANDS', attrs=['bold'])}\n"
            f"\n"
            f"    add feature-store        Registers a new feature store with Potman.\n"
            f"\n"
            f"    display config           Prints the 'raw' JSON configuration of Potman.\n"
            f"\n"
            f"    display potman-dir       Prints the path of the potman directory, which contains the configuration\n"
            f"                             as well as cloned feature repositories.\n"
            f"\n"
            f"    exit|quit                Terminates the Potman CLI.\n"
            f"\n"
            f"    list feature-stores      Lists all known feature stores.\n"
            f"\n"
            f"    pull                     Performs a pull for all feature stores.\n"
            f"\n"
            f"    remove feature-store ID  Removes the feature store with the specified ID from Potman."
    )

    _PROMPT_PREFIX: Final[str] = "potman> "
    """The prompt prefix used for user inputs in the terminal."""

    #  METHODS  ########################################################################################################

    def __init__(self) -> None:

        self._observers: list[view_observer.ViewObserver] = []
        self._quit = False

    #  METHODS  ########################################################################################################

    def _fetch_potman_version(self) -> Optional[str]:

        try:

            pkg_resources.get_distribution("potman").version

        except pkg_resources.DistributionNotFound:

            return None

    def _notify_observers(self, action: actions.Action):

        for observer in self._observers:

            observer.action_performed(action)

    def _parse_command(self, command: str) -> Optional[actions.Action]:

        if command == "add feature-store":

            return actions.AddFeatureStoreStartAction()

        elif command == "display config":

            return actions.PrintConfigAction()

        elif command == "display potman-dir":

            return actions.PrintPotmanDirAction()

        elif command == "help":

            return actions.PrintHelpAction()

        elif command == "list feature-stores":

            return actions.ListFeatureStoresAction()

        elif command == "pull":

            return actions.PullAction()

        elif (
                command == "q" or
                command == "quit" or
                command == "exit" or
                command == "x"
        ):

            return actions.QuitAction()

        elif self._REMOVE_FEATURE_STORE_REGEX.match(command):

            match = self._REMOVE_FEATURE_STORE_REGEX.match(command)
            feature_store_id = match.group("id")
            return actions.RemoveFeatureStoreAction(feature_store_id)

    def _print_banner(self) -> None:
        """TODO: docs"""

        banner = resources.read_text("potman.cli.resources", "banner.txt")
        potman_version = self._fetch_potman_version() or "???"

        print()
        print(banner)
        print()
        print(f"POTMAN CLI v{potman_version}")
        print("\n")

    def _read_command(self) -> str:

        while True:

            command = input(self._PROMPT_PREFIX).strip()
            if command:

                return command

    def _run(self) -> None:

        while not self._quit:

            try:

                command = self._read_command()
                action = self._parse_command(command)

                if action:

                    self.trigger_action(action)

                else:

                    self.print_error_message(f"Unknown command <{command}>")
                    print("Type <help> to display the help text")

            except EOFError:

                print()
                self.trigger_action(actions.QuitAction())

            except KeyboardInterrupt:

                print()

    def display_feature_stores(self, feature_stores: Iterable[config.FeatureStoreConfig]) -> None:

        num_feature_stores = sum(1 for _ in feature_stores)
        print()
        print(
                tabulate.tabulate(
                        [[x.id, x.project_name, x.clone_url, x.aws_profile, x.last_pull] for x in feature_stores],
                        headers=["ID", "Project Name", "Clone URL", "AWS Profile", "Last Pull"]
                )
        )
        print(f"({num_feature_stores} rows)")
        print()

    def print_config(self, cfg: config.PotmanConfig) -> None:

        json_config = anyjsonthing.Serializer.to_json(cfg)

        print()
        print(json.dumps(json_config, indent=4))
        print()

    def print_error_message(self, message: str) -> None:

        termcolor.cprint(message, "red")

    def print_help(self) -> None:

        print()
        print(self._HELP_TEXT)
        print()

    def print_success_message(self, message: str) -> None:

        termcolor.cprint(message, "green")

    def print_text(self, text: str) -> None:

        print(text)

    def prompt_input(self, instruction: str, default_value: Optional[str] = None) -> str:

        prompt = f"{instruction} "
        if default_value is not None:

            prompt += f"[{default_value}] "

        return input(prompt)

    def register_observer(self, observer: view_observer.ViewObserver) -> None:
        """Registers the provided ``observer`` with this :class:`~.View`."""

        self._observers.append(observer)

    def run_add_feature_store_workflow(self) -> None:

        workflows.AddFeatureStoreWorkFlow(self).run()

    def trigger_action(self, action: actions.Action) -> None:

        self._notify_observers(action)

    def start(self) -> None:
        """Starts the view."""

        self._print_banner()
        self._run()
        print("Bye bye!")

    def stop(self) -> None:
        """Stops the view."""

        self._quit = True
