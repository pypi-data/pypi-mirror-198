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
from rich.prompt import Confirm, Prompt
from typing import List, Optional
import typer

from tui_rsync.cli.label_prompt import LabelPrompt
from tui_rsync.cli.rsync import Rsync
from tui_rsync.models.models import Group, count_all_labels_except

console = Console()
groups = typer.Typer()

@groups.command()
def add(
    group_label: str = typer.Option(
        None, "--group-label", "-g",
        help="[b]The label[/] is a uniq identification of a [b]group[/].",
        show_default=False
    ),
):
    """
    [green b]Create[/] a [yellow]new group[/] with a [bold]uniq[/] label.
    [b]The chosen sources[/] will be united into [b]the group[/].
    """
    if group_label is None:
        question = "Would you like to change [yellow b]the group label[/]?"
        group_label = LabelPrompt.ask_uuid(question)

    labels = []
    while True:
        is_empty = count_all_labels_except(labels) == 0
        if is_empty:
            break
        is_fzf = Confirm.ask("Would you like to add a source to the group? ",
                             default=True)
        if not is_fzf:
            break
        option = LabelPrompt.get_label_except_fzf(labels)
        labels.append(option)
    Group.create_save(group_label, labels)

