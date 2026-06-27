"""
help.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import sys
# Function to display help
def print_help():
    """
    help function
    """
    help_message = """
Usage: dircomply [OPTIONS]
       dircomply [folder1_path] [folder2_path] [OPTIONS]

A small package to compare the files between two project folders.

Options:
    --version, -v      Show the version of dircomply and exit
    --help, -h         Show this help message and exit
    --email, -e        Show email and exit
    --author, -a       Show author and exit
    (No arguments)     Launch the GUI application
    [folder1_path] [folder2_path] compare contents from both folders.

Compare option overrides:
    --content_ext VALUE             Overwrite JSON content_extensions
    --append_content_ext VALUE      Append to JSON content_extensions
    --existence_ext VALUE           Overwrite JSON existence_extensions
    --append_existence_ext VALUE    Append to JSON existence_extensions
    --skip_dir VALUE                Overwrite JSON skip_dirs
    --append_skip_dir VALUE         Append to JSON skip_dirs

VALUE can be comma-separated or the flag can be repeated.
Examples:
    dircomply old new --append_skip_dir dist --append_content_ext .toml,.cfg
    dircomply old new --skip_dir .git,build --content_ext .py --content_ext .json
    """
    print(help_message)
    sys.exit(0)
    