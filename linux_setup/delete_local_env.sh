#!/bin/bash
set -e

############################################
# Get script file directory
# place where the scripts located.
############################################
script_path="$(realpath "${BASH_SOURCE[0]}")"
script_dir="$(dirname "$script_path")"

############################################
# Set root dir (parent of script_dir)
############################################
root_dir="$(dirname "$script_dir")"
cd "$root_dir"

############################################
# Got config variables from env_config file
############################################
source "$script_dir/env_config.sh"

############################################
# Get current dir name
# it is based on the root dir and python version
############################################
root_folder_name="$(basename "$root_dir")"

# Set the environment name
env_name="${root_folder_name}-py${python_version}-env"

############################################
# Check if env already exists
############################################
venv_path="$HOME/envs/$env_name"

if [ -d "$venv_path" ]; then
    echo "Deleting environment - $venv_path"
else
    echo "No venv. Run local_setup first."
    exit 1
fi

############################################
# Delete the environment
############################################
rm -rf "$venv_path"
echo "Environment deleted"
