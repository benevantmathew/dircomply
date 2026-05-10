"""
utils.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os
import json

def get_files_with_extensions(folder, extensions, skip_dirs=None):
    """
    Get all files with specific extensions,
    skipping directory names at any depth.
    """

    skip_dirs = set(skip_dirs or [])

    all_files = set()

    for root_dir, dirs, files in os.walk(folder):

        # modify dirs in-place
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            if file.endswith(extensions):
                relative_path = os.path.relpath(
                    os.path.join(root_dir, file),
                    folder
                )
                all_files.add(relative_path)

    return all_files

def load_extensions(ext_json_filepath):
    """
    Load extensions to compare.
    - "content_extensions" are compared by file contents
    - "existence_extensions" are only checked for presence
    - "skip_dirs" are skipped on all levels
    """
    with open(ext_json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return (
        tuple(data.get("content_extensions", [])),
        tuple(data.get("existence_extensions", [])),
        tuple(data.get("skip_dirs", []))
    )
