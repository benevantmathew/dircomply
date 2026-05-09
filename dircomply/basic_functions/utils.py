"""
utils.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os
import json

def get_files_with_extensions(folder, extensions):
    """
    get_files_with_extensions
    # Function to get all files with specific extensions
    """
    all_files = set()
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.endswith(extensions):
                relative_path = os.path.relpath(os.path.join(root_dir, file), folder)
                all_files.add(relative_path)
    return all_files

def load_extensions(ext_json_filepath):
    """
    Load extensions to compare.
    - "content_extensions" are compared by file contents
    - "existence_extensions" are only checked for presence
    """
    with open(ext_json_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return (
        tuple(data.get("content_extensions", [".txt", ".py", ".bat", ".html", ".ts"])),
        tuple(data.get("existence_extensions", [".xlsx", ".csv", ".docx"]))
    )
