from __future__ import unicode_literals

from rich.console import Console
from selectmenu import SelectMenu


def menuOptions():
    console = Console()
    console.print(":computer: Welcome to machine learning application :computer:", style="BOLD GREEN")
    menu = SelectMenu()
    menu.add_choices([
        "1. Basic Python",
        "2. Intermediate Python",
        "3. Advanced Python"
    ])
    result = menu.select("Choice languages")
    return result


if __name__ == '__main__':
    menuOptions()
