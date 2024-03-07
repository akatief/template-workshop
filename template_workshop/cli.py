"""CLI interface for template_workshop project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
##### YOUR CODE HERE #####
import sys
from template_workshop import Fibonacci
##########################



def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m template_workshop` and `$ template_workshop `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    ##### YOUR CODE HERE #####
    # Get the command-line argument for n
    if len(sys.argv) != 2:
        print("Usage: template_workshop <n>")
        sys.exit(1)
    
    n = int(sys.argv[1])  # Convert the command-line argument to an integer

    fib = Fibonacci()
    print(fib.fib(n))
    ##########################