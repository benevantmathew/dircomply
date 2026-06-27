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
        self._copy_missing_config(
            paths.get_extension_filepath(),
            "dircomply.application",
            "extensions.json",
            paths.get_sample_extension_filepath()
        )
        self._copy_missing_config(
            paths.get_settings_filepath(),
            "dircomply.application",
            "settings.json",
            paths.get_sample_settings_filepath()
        )

    def _copy_missing_config(self, target_filepath, resource_package, resource_name, fallback_filepath):
        """
        Copy a bundled config file to the user config folder if it is missing.
        """
        if os.path.exists(target_filepath):
            return

        resource = (
            importlib.resources.files(resource_package)
            .joinpath(resource_name)
        )

        if resource.is_file():
            with importlib.resources.as_file(resource) as src:
                shutil.copy2(src, target_filepath)
        else:
            shutil.copy2(fallback_filepath, target_filepath)
