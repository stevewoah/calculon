import re, sys

def validate_args(args: list[str]) -> str:
    """
    Validates the command-line arguments and joins them into an expression string. Removes the first entry of the input list.

    Args:
        args (list[str]): List of arguments passed from CLI.

    Returns:
        str: A string representing the mathematical expression to evaluate.

    Raises:
        SystemExit: If no arguments are provided.
    """
    if len(args) < 2:
        print("Usage: calculon \"3 + 4 * 2\"")
        sys.exit(1)

    expression = " ".join(sys.argv[1:])

    return expression

def calculate_expression(expression):
    try:
        # Regular expression to validate input
        if not re.match(r'^[0-9+\-*/. ]+$', expression):
            print("Invalid characters in input.")
            return
        
        # Respect operator precedence
        result = eval(expression)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Error: {e}")

def calc(args):
    calculate_expression(validate_args(args))