"""
config.py

Author: Benevant Mathew
Date: 2025-09-21
"""
import os

from dircomply.basic_functions.os_funs import get_user_profile
from dircomply.paths_manager.paths_manager import PathsManager
from dircomply.utils import load_extensions

# main directories
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__)) # directory where config file exist
USRPROFILE = get_user_profile()  # user directory
ROOT_DIR = os.path.join(CURRENT_DIR, "..")  # root directory

# definining PathsManager object
def get_paths():
    """
    create paths instances
    """
    return PathsManager(ROOT_DIR, USRPROFILE)

# definining PathsManager object
paths = get_paths()

# load extensions
content_exts, existence_exts = load_extensions()

class Config:
    """
    config class
    """
    #  APP details
    pass


### Initiated common config object
config = Config()
