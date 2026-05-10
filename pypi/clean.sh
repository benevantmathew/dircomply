#!/bin/bash

# Get script file directory
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Cleaning build directories..."

# Run the clean.py script to remove old build artifacts
python "$script_dir/clean.py"

echo "Done!"
