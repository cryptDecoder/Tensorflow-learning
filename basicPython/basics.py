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
    name = "JOHN"
    console.log("let's see how python is working\n")
    time.sleep(2)
    console.log("Putting your name into the print function")
    time.sleep(2)
    print(f">> Hello {name}")
    time.sleep(3)
    console.print("## VARIABLES IN PYTHON ##", style="BOLD BLUE")
    variables = """
            variable is used to store the values
    """
    console.print("example x=100")
    console.print("## DATA TYPES IN PYTHON ##", style="BOLD BLUE")
    variables = """
                Specifies the type of data stored into the variable
        """
    console.print("""
        if x = 100 it should be integer \n
        if name = "JOHN" it should be string \n 
        if flag = True it should be boolean \n 
        if names = ["JOHN","JAKE","CHAMP"] it should be list \n
        if colors = ("RED","YELLOW","GREEN") is should be tupple \n
        if employee = {
                        "id": "1,"
                       "name": "TOM"
                        "city": "TX" 
                       }
    """)
    console.print("This is all about DATA TYPES in python")
