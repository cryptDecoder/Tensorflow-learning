import time

from rich.console import Console

console = Console()


def flowcontrolInpython():
    console.print("## PYTHON CONTROL FLOW ##", style="BOLD CYAN")
    console.print("Flow control is used to execute the conditional statement")
    console.print("For example if age > 18 you are eligible for vote otherwise you are not")
    console.print("let's see with example in python")
    time.sleep(2)
    console.print("""
                    start
                      |
                    if age >  18 
                        Your are eligible for vote
                    else
                        You are not eligible for vote
                     |
                    end  
                """)
    time.sleep(2)
    console.log(" Lets  execute the python code ")
    age = 19
    if age > 18:
        print("You are eligible for vote")
    else:
        print("You are not eligible for vote")

    pass
