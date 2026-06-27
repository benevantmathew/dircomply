"""
compare.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os

from dircomply.application.config import paths
from dircomply.basic_functions.utils import get_files_with_extensions, load_extensions
from dircomply.basic_functions.read import read_file


def _merge_values(base_values, overwrite_values=None, append_values=None):
    """
    Apply overwrite/append command-line values on top of JSON values.
    """
    values = overwrite_values if overwrite_values else base_values
    merged_values = list(values) + list(append_values or [])

    # De-duplicate while preserving order.
    return tuple(dict.fromkeys(merged_values))


def compare_folders(
        folder1,
        folder2,
        content_exts=None,
        append_content_exts=None,
        existence_exts=None,
        append_existence_exts=None,
        skip_dirs=None,
        append_skip_dirs=None
    ):
    """
    compare_folders
    Function to compare folders

    Values from extensions.json are used by default. Optional arguments can
    overwrite those JSON values or append additional values for this compare.
    """
    # load extensions(for each query)
    ext_json_filepath = paths.get_extension_filepath()
    json_content_exts, json_existence_exts, json_skip_dirs = load_extensions(ext_json_filepath)

    content_exts = _merge_values(json_content_exts, content_exts, append_content_exts)
    existence_exts = _merge_values(json_existence_exts, existence_exts, append_existence_exts)
    skip_dirs = _merge_values(json_skip_dirs, skip_dirs, append_skip_dirs)

    # Separate by category
    folder1_content = get_files_with_extensions(folder1, content_exts, skip_dirs)
    folder2_content = get_files_with_extensions(folder2, content_exts, skip_dirs)

    folder1_exist = get_files_with_extensions(folder1, existence_exts, skip_dirs)
    folder2_exist = get_files_with_extensions(folder2, existence_exts, skip_dirs)

    # Combine sets
    folder1_files = folder1_content | folder1_exist
    folder2_files = folder2_content | folder2_exist

    # Common files
    common_files = folder1_files & folder2_files

    # Unique files
    unique_to_folder1 = folder1_files - folder2_files
    unique_to_folder2 = folder2_files - folder1_files

    different_files = []

    # Only compare contents for content_exts
    for file in common_files:
        if file.endswith(content_exts):
            path1 = os.path.join(folder1, file)
            path2 = os.path.join(folder2, file)
            if read_file(path1) != read_file(path2):
                different_files.append(file)

    return sorted(different_files), sorted(unique_to_folder1), sorted(unique_to_folder2)
