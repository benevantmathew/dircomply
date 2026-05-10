#!/bin/bash
set -e  # Exit immediately on error

echo "================================="
echo "Welcome to setup. This setup will:"
echo "- Ensures Python version"
echo "- Create a local virtual environment"
echo "- You can rerun this safely."
echo "================================="

##############################################################################
# Resolve paths
script_path="$(realpath "${BASH_SOURCE[0]}")"
script_dir="$(dirname "$script_path")"
project_dir="$(dirname "$script_dir")"

##############################################################################
# Load config
config_file="$script_dir/env_config.sh"
if [ -f "$config_file" ]; then
    source "$config_file"
else
    echo "ERROR: env_config.sh not found in $script_dir"
    exit 1
fi

##############################################################################
# Ensure pyenv is installed
if ! command -v pyenv >/dev/null 2>&1; then
    cat <<EOF
ERROR: pyenv not found.

Please install pyenv manually before running this script.
See: https://github.com/pyenv/pyenv

Example (user install):
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    export PYENV_ROOT="\$HOME/.pyenv"
    export PATH="\$PYENV_ROOT/bin:\$PATH"
    eval "\$(pyenv init -)"

EOF
    exit 1
fi

##############################################################################
# Fail fast if pyenv is not usable
command -v pyenv >/dev/null 2>&1 || {
    echo "ERROR: pyenv is not available in this shell."
    echo "Make sure pyenv is initialized in your shell profile."
    exit 1
}

##############################################################################
# Initialize pyenv for the current shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

##############################################################################
# Ensure required Python version is installed
echo "Python version configured: $python_version"

if ! pyenv versions --bare | grep -qx "$python_version"; then
    echo "Installing Python $python_version via pyenv..."
    pyenv install "$python_version"
fi

##############################################################################
# Activate Python version locally for this shell
pyenv shell "$python_version"

##############################################################################
if ! python - <<'EOF'
import venv
EOF
then
    echo "ERROR: Python venv module is not available."
    echo "This Python was likely built without ensurepip or venv support."
    echo "Rebuild Python with proper dependencies (openssl, zlib, ensurepip)."
    exit 1
fi

##############################################################################
# Determine virtualenv name and path
folder_name="$(basename "$project_dir")"
venv_name="${folder_name}-py${python_version}-env"
venv_path="${HOME%/}/envs/$venv_name"

##############################################################################
# Create virtual environment if needed
if [ -d "$venv_path" ]; then
    echo "Virtual environment already exists: $venv_path"
else
    echo "Creating virtual environment at: $venv_path"
    mkdir -p "$(dirname "$venv_path")"

    python -m venv "$venv_path" || {
        echo "ERROR: Failed to create virtual environment at $venv_path"
        exit 1
    }
fi

##############################################################################
# Upgrade pip inside the virtual environment
echo "Upgrading pip inside the virtual environment..."
source "$venv_path/bin/activate"
python -m pip install --upgrade pip
deactivate

echo "================================="
echo "Virtual environment setup completed successfully."
echo "Venv location: $venv_path"
echo "================================="
