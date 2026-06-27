"""
main.py

Author: Benevant Mathew
Date: 2025-09-20
"""
import argparse
import os
import sys

from dircomply.version import (
    __version__,__email__,__release_date__,__author__
)
from dircomply.core.help import print_help


def _split_values(values):
    """
    Split repeated comma-separated CLI values into a clean tuple.
    """
    split_items = []
    for value in values or []:
        split_items.extend(item.strip() for item in value.split(","))
    return tuple(item for item in split_items if item)


def _normalize_extensions(values):
    """
    Accept both "py" and ".py" extension input forms.
    """
    return tuple(
        value if value.startswith(".") else f".{value}"
        for value in _split_values(values)
    )


def _parse_args(argv):
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("folders", nargs="*")
    parser.add_argument("--content_ext", action="append", default=[])
    parser.add_argument("--append_content_ext", action="append", default=[])
    parser.add_argument("--existence_ext", "--existance_ext", action="append", default=[])
    parser.add_argument("--append_existence_ext", "--append_existance_ext", action="append", default=[])
    parser.add_argument("--skip_dir", action="append", default=[])
    parser.add_argument("--append_skip_dir", action="append", default=[])
    return parser.parse_args(argv)


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

    args = _parse_args(sys.argv[1:])

    # initiate
    folder1_path = None
    folder2_path = None
    compare_on_start = True

    if len(args.folders) == 1:
        print("Error: Please provide both folder paths.")
        sys.exit(1)
    if len(args.folders) > 2:
        print("Error: Please provide only two folder paths.")
        sys.exit(1)

    if len(args.folders) == 2:
        folder1_path = args.folders[0]
        folder2_path = args.folders[1]
        if not os.path.exists(folder1_path):
            print(f"Error: Directory '{folder1_path}' does not exist.")
            sys.exit(1)
        if not os.path.exists(folder2_path):
            print(f"Error: Directory '{folder2_path}' does not exist.")
            sys.exit(1)

    compare_options = {
        "content_exts": _normalize_extensions(args.content_ext),
        "append_content_exts": _normalize_extensions(args.append_content_ext),
        "existence_exts": _normalize_extensions(args.existence_ext),
        "append_existence_exts": _normalize_extensions(args.append_existence_ext),
        "skip_dirs": _split_values(args.skip_dir),
        "append_skip_dirs": _split_values(args.append_skip_dir),
    }

    # Add startup
    from dircomply.core.startup import Startup
    startup_obj = Startup()
    startup_obj.start()

    # call gui
    from dircomply.gui.gui import create_gui
    create_gui(
        folder1_path=folder1_path,
        folder2_path=folder2_path,
        compare_on_start=compare_on_start,
        compare_options=compare_options
    )

if __name__ == "__main__":
    main()
