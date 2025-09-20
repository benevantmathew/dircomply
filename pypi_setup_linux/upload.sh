#!/bin/bash
set -e  # exit immediately on error

# Get script file dir
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Set root dir (one level up)
rootdir="$script_dir/.."

# cd to root dir
cd "$rootdir"

echo "Cleaning build directories..."

# Run the clean.py script to remove old build artifacts
python pypi_setup/clean.py

echo "Building distribution packages..."
python setup.py sdist bdist_wheel

echo "Uploading to PyPI..."
twine upload dist/*

echo "Done!"
