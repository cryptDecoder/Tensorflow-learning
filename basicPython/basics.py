# standard import here
import time

from rich.console import Console

console = Console()


def helloPython():
    console.print("## PRINTING A MESSAGE TO THE SCREEN ##", style="BOLD BLUE")
    printfunc = "" \
                "In python print() function is used to print the message on screen \n" \
                "how to use print function ? \n" \
                "print(YOUR MESSAGE) your message should be in string format like always put message with single or double qputes. \n" \
                "" \
                ""
    console.print(printfunc, style="BOLD YELLOW")
    console.print("Let's get print your name here !", style="BOLD green")
    name = console.input("Enter your name :\n")
    console.log("let's see how python is working\n")
    time.sleep(2)
    console.log("Putting your name into the print function")
    time.sleep(2)
    print(f">> Hello {name}")
