#!/bin/bash

##############################################################################
# Load environment config
script_path="$(realpath "${BASH_SOURCE[0]}")"
script_dir="$(dirname "$script_path")"
project_dir="$(dirname "$script_dir")"

# Source config
config_file="$script_dir/env_config.sh"
if [ -f "$config_file" ]; then
    . "$config_file"
else
    echo "env_config.sh not found in $script_dir"
    return 1 2>/dev/null || exit 1
fi

##############################################################################
# Check Python version
echo "Python version configured: $python_version"

# Determine venv name
folder_name="$(basename "$project_dir")"
venv_name="${folder_name}-py${python_version}-env"
venv_path="$HOME/envs/$venv_name"

# Activate virtual environment
if [ -d "$venv_path" ]; then
    echo "Activating virtual environment: $venv_name"
    . "$venv_path/bin/activate"
else
    echo "Virtual environment not found: $venv_path"
    echo "Please run local_setup.sh first."
    return 1 2>/dev/null || exit 1
fi

# Move to project root (one level above script dir)
cd "$project_dir" || {
    echo "Failed to cd to $project_dir"
    return 1 2>/dev/null || exit 1
}
