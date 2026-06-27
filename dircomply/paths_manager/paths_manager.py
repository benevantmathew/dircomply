"""
paths_manager.py

Author: Benevant Mathew
Date: 2026-05-09
"""

import os

from dircomply.version import __app_name__

class PathsManager:
    """
    Paths manager class
    """
    def __init__(self, root_dir, userprofile):
        # folders
        self.root_dir = root_dir
        self.userprofile = userprofile

        # XDG standard
        self.xdg_config_folder = os.path.join(self.userprofile, ".config")
        self.app_folder = os.path.join(self.xdg_config_folder, __app_name__)

        # Ensure directories exist
        for d in [
            self.xdg_config_folder,
            self.app_folder,
        ]:
            os.makedirs(d, exist_ok=True)

    def get_extension_filepath(self):
        """
        get extension filepath
        """
        return os.path.join(self.app_folder,"extensions.json")

    def get_sample_extension_filepath(self):
        """
        used to get the factory extension.json filepath
        """
        return os.path.join(self.root_dir,"application","extensions.json")

    def get_settings_filepath(self):
        """
        get settings filepath
        """
        return os.path.join(self.app_folder,"settings.json")

    def get_sample_settings_filepath(self):
        """
        used to get the factory settings.json filepath
        """
        return os.path.join(self.root_dir,"application","settings.json")
