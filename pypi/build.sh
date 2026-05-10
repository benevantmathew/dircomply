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

echo "Cleaning build directories..."

# Run the clean.py script to remove old build artifacts
python pypi/clean.py

echo "Building distribution packages..."
python -m build

# Find the latest .whl file in dist folder (sorted by time, newest first)
latest_whl=$(ls -t dist/*.whl | head -n 1)

if [[ ! -f "$latest_whl" ]]; then
    echo "ERROR: No wheel file found in dist directory!"
    exit 1
fi

echo "Installing package locally..."
pip install --force-reinstall "$latest_whl"

echo "Done!"
