"""
main.py

Author: Benevant Mathew
Date: 2025-09-20
"""
import os
import sys

from dircomply.version import (
    __version__,__email__,__release_date__,__author__
)
from dircomply.core.help import print_help

# Main entry point
def main():
    """
    main
    """
    # Check for command-line arguments
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"version {__version__}")
        sys.exit(0)
    if "--help" in sys.argv or "-h" in sys.argv:
        print_help()
        sys.exit(0)
    if "--author" in sys.argv or "-a" in sys.argv:
        print(f"Author {__author__}")
        sys.exit(0)
    if "--email" in sys.argv or "-e" in sys.argv:
        print(f"Mailto {__email__}")
        sys.exit(0)
    if "--date" in sys.argv or "-d" in sys.argv:
        print(f"Release Date {__release_date__}")
        sys.exit(0)
    if len(sys.argv) == 2:
        print("Error: Please provide both folder paths.")
        sys.exit(1)

    # initiate
    folder1_path = None
    folder2_path = None
    compare_on_start = True

    if len(sys.argv) > 2:
        folder1_path = sys.argv[1]
        folder2_path = sys.argv[2]
        if not os.path.exists(folder1_path):
            print(f"Error: Directory '{folder1_path}' does not exist.")
            sys.exit(1)
        if not os.path.exists(folder2_path):
            print(f"Error: Directory '{folder2_path}' does not exist.")
            sys.exit(1)

    # Add startup
    from dircomply.core.startup import Startup
    startup_obj = Startup()
    startup_obj.start()

    # call gui
    from dircomply.gui.gui import create_gui
    create_gui(
        folder1_path=folder1_path,
        folder2_path=folder2_path,
        compare_on_start=compare_on_start
    )

if __name__ == "__main__":
    main()
