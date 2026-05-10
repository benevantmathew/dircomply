"""
main.py

Author: Benevant Mathew
Date: 2026-05-09
"""
import os
import shutil
import importlib.resources

from dircomply.application.config import paths

class Startup:
    """
    A class to handle the initialization of the dircomply application,
    including xdg folder creation
    """

    def __init__(self):
        """
        Initialize the Startup instance.
        """
        pass

    def start(self):
        """
        Startup steps
        """
        ext_json_filepath = paths.get_extension_filepath()
        # check extension json file exist in app directory
        # if not copy it to app directory
        if not os.path.exists(ext_json_filepath):
            resource = (
                importlib.resources.files("dircomply.application")
                .joinpath("extensions.json")
            )

            if resource.is_file():
                with importlib.resources.as_file(resource) as src:
                    shutil.copy2(src, ext_json_filepath)
            else:
                sample_ext_filepath = paths.get_sample_extension_filepath()
                shutil.copy2(sample_ext_filepath, ext_json_filepath)
