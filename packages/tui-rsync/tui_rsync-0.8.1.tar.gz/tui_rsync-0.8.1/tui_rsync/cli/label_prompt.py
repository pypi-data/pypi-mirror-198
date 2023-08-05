################################################################################
# Copyright (C) 2023 Kostiantyn Klochko <kostya_klochko@ukr.net>               #
#                                                                              #
# This file is part of tui-rsync.                                              #
#                                                                              #
# tui-rsync is free software: you can redistribute it and/or modify it under   #
# uthe terms of the GNU General Public License as published by the Free        #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# tui-rsync is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more        #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU General Public License along with #
# tui-rsync. If not, see <https://www.gnu.org/licenses/>.                      #
################################################################################

from rich.console import Console
from rich.prompt import Prompt
from pyfzf import FzfPrompt
import uuid
from tui_rsync.models.models import all_labels, all_labels_except

console = Console()

class LabelPrompt:
    @staticmethod
    def ask_uuid(
        question: str = "Would you like to change [yellow b]the label[/]?"
    ) -> str:
        """
        Return the label or the default uuid value.
        """
        uid = uuid.uuid4().hex
        label = Prompt.ask(question, default=uid)
        return label

    @staticmethod
    def get_label_fzf() -> str:
        fzf = FzfPrompt()
        return fzf.prompt(all_labels().iterator())[0]

    @staticmethod
    def get_label_except_fzf(labels = None) -> str:
        fzf = FzfPrompt()
        return fzf.prompt(all_labels_except(labels).iterator())[0]
