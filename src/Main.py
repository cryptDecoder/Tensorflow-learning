from __future__ import unicode_literals

from rich.console import Console
from selectmenu import SelectMenu

from basicPython import basics, flowControl, pythonFunctions


def menuOptions():
    console = Console()
    console.print(":computer: Welcome to machine learning application :computer:", style="BOLD GREEN")
    menu = SelectMenu()
    menu.add_choices([
        "1. Introduction to Python",
        "2. Intermediate Python",
        "3. Advanced Python"
    ])
    result = menu.select("Choice languages")

    if result == "1. Introduction to Python":
        console.log(":computer: Welcome to Basic python section", style="BOLD Cyan")
        submenu = SelectMenu()
        submenu.add_choices([
            "1. Python Introduction",
            "2. Python Flow Control",
            "3. Python Functions",
            "4. Python Datatypes in depth",
            "5. Python Files",
            "6. Python Object & Class",
            "7. Python Advanced Topics",
            "8. Python Date and time"
        ])
        basicTopics = submenu.select("Choice topic to learn")
        if basicTopics == "1. Python Introduction":
            basics.helloPython()
        elif basicTopics == "2. Python Flow Control":
            flowControl.flowcontrolInpython()
        elif basicTopics == "3. Python Functions":
            pythonFunctions.pythonFunctions()


if __name__ == '__main__':
    menuOptions()
