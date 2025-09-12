#!/bin/bash
set -e #fail fast."Exit the script immediately if any command returns a non-zero (i.e., error) exit status."

echo "================================="
echo "Welcome to setup. This setup will:"
echo "- Create a local virtual environment"
echo "- You can rerun this safely."
##############################################################################
# Load config
script_path="$(realpath "${BASH_SOURCE[0]}")"
script_dir="$(dirname "$script_path")"
project_dir="$(dirname "$script_dir")"

config_file="$script_dir/env_config.sh"
if [ -f "$config_file" ]; then
    . "$config_file"
else
    echo "env_config.sh not found in $script_dir"
    return 1 2>/dev/null || exit 1
fi

##############################################################################
# Ensure pyenv is installed
if ! command -v pyenv &>/dev/null; then
    echo "pyenv not found. Trying to install it via pacman..."

    if command -v pacman &>/dev/null; then
        sudo pacman -S --needed pyenv || { echo "Failed to install pyenv"; exit 1; }
    elif command -v yay &>/dev/null; then
        yay -S --needed pyenv || { echo "Failed to install pyenv"; exit 1; }
    else
        echo "Neither yay nor pacman available to install pyenv."
        exit 1
    fi
fi

# Ensure Python build requirements exist
echo "Checking for Python build dependencies..."
if command -v pacman &>/dev/null; then
    sudo pacman -S --needed base-devel || { echo "Failed to install Python build requirements"; exit 1; }
elif command -v yay &>/dev/null; then
    yay -S --needed base-devel || { echo "Failed to install Python build requirements"; exit 1; }
else
    echo "Neither yay nor pacman available to install build requirements."
    exit 1
fi
##############################################################################
# Ensure Python build dependencies are installed (Arch Linux)
if command -v pacman &>/dev/null || command -v yay &>/dev/null; then
    build_deps=(
        base-devel
        zlib
        xz
        tk
        gdbm
        libffi
        bzip2
        openssl
    )

    missing_pkgs=()
    for pkg in "${build_deps[@]}"; do
        if ! pacman -Qi "$pkg" &>/dev/null; then
            missing_pkgs+=("$pkg")
        fi
    done

    if [ "${#missing_pkgs[@]}" -gt 0 ]; then
        echo "Installing missing Python build dependencies: ${missing_pkgs[*]}"
        if command -v pacman &>/dev/null; then
            sudo pacman -S --needed "${missing_pkgs[@]}"
        else
            yay -S --needed "${missing_pkgs[@]}"
        fi
    else
        echo "All required Python build dependencies are already installed."
    fi
else
    echo "WARNING: Could not detect pacman or yay. Skipping build dependency check."
fi

##############################################################################
# Initialize pyenv for the current shell
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

##############################################################################
# Check and install required Python version using pyenv
echo "Python version configured: $python_version"
if ! pyenv versions --bare | grep -qx "$python_version"; then
    echo "Installing Python $python_version via pyenv..."
    pyenv install "$python_version" || {
        echo "Failed to install Python $python_version"
        exit 1
    }
fi

pyenv shell "$python_version" || {
    echo "pyenv could not activate Python $python_version"
    exit 1
}

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
    mkdir -p "$(dirname "$venv_path")"  # Ensure the parent folder exists
    python -m venv "$venv_path" || {
        echo "Failed to create virtualenv"
        exit 1
    }
fi

##############################################################################
# Upgrade pip in the virtual environment
echo "Activating venv and upgrading pip..."
source "$venv_path/bin/activate"
python -m pip install --upgrade pip
deactivate

echo "Virtual environment setup completed."
