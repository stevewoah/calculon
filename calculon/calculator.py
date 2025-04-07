"""Business logic for calculon"""

import re
import sys


def validate_args(args: list[str]) -> str:
    """
    Validates the command-line arguments and joins them into an expression string. Removes the
    first entry of the input list.

    Args:
        args (list[str]): List of arguments passed from CLI.

    Returns:
        str: A string representing the mathematical expression to evaluate.

    Raises:
        SystemExit: If no arguments are provided.
    """
    if len(args) < 2:
        print('Usage: calculon "3 + 4 * 2"')
        sys.exit(1)

    expression = " ".join(sys.argv[1:])

    return expression


def calculate_expression(expression):
    """
    Evaluates a mathematical expression string and prints the result.

    The function supports the four basic arithmetic operations: addition,
    subtraction, multiplication, and division. Operator precedence is respected
    (e.g., multiplication is evaluated before addition). Only digits, spaces,
    decimal points, and the operators '+', '-', '*', and '/' are allowed.

    Args:
        expression (str): A string containing a mathematical expression (e.g., "3 + 4 * 2").

    Returns:
        None: The result is printed directly. Error messages are also printed
        if the input is invalid or a division by zero occurs.
    """
    try:
        # Regular expression to validate input
        if not re.match(r"^[0-9+\-*/. ]+$", expression):
            print("Invalid characters in input.")
            return

        # Just for the sake of testing it
        # pylint: disable=eval-used
        result = eval(expression)
        # pylint: enable=eval-used

        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input value.")
    except SyntaxError:
        print("Error: Invalid syntax in the expression.")


def calc(args):
    """
    Validates command-line arguments and calculates the result of the provided expression.

    This function takes the command-line arguments (usually passed through `sys.argv`),
    validates the expression, and then calls `calculate_expression` to evaluate the expression.

    Args:
        args (list): A list of command-line arguments, typically provided by `sys.argv[1:]`.
                      The list should contain a mathematical expression as a string to be evaluated.

    Returns:
        None: The result of the expression is printed directly. If there is an error (e.g., invalid input or
              syntax), an error message is printed instead.
    """
    calculate_expression(validate_args(args))
