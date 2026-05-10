#!/bin/bash
set -e  # exit immediately on error
set -x  # print commands as they run

# Ensure required build tools are installed in this venv
python -m pip install --upgrade --upgrade-strategy only-if-needed build twine setuptools

# Get script file dir
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Set root dir (one level up)
rootdir="$script_dir/.."

# cd to root dir
cd "$rootdir"

# Run the clean.py script to remove old build artifacts
python pypi/clean.py

# build
echo "Building distribution packages..."
python setup.py sdist bdist_wheel

# upload to pypi
echo "Uploading to PyPI..."
twine upload dist/*

echo "Done!"
