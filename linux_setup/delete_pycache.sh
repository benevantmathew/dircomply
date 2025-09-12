#!/bin/bash
set -e

############################################
# Get script file directory
# place where the scripts located.
############################################
script_path="$(realpath "${BASH_SOURCE[0]}")"
script_dir="$(dirname "$script_path")"

#####################################
# Define the root folder (parent)
#####################################
rootdir="$(dirname "$script_dir")"

#####################################
# Find and delete all __pycache__ folders
#####################################
find "$rootdir" -type d -name '__pycache__' -print -exec rm -rf {} +

echo "Cleanup complete."
exit 0
