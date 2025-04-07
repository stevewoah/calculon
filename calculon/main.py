"""Main entry for calculon"""

import sys
from calculon.calculator import calc


def main():
    """
    Main entry point of calculon.

    Performs a mathematical equotation based on the command line arguments and prints it to the
    command line.
    e. g. 3 + 5, "3 + 5", 3 "+ 5"

    Raises:
        SystemExit: If no arguments are provided.
    """
    return calc(sys.argv[1:])


if __name__ == "__main__":
    main()
