"""
dircomply/basic_functions/os_funs.py

Author: Benevant Mathew
Date: 2026-05-09
"""
import os
import platform


# OS file related functions
def get_user_profile():
    """
    Docstring for get_user_profile
    """
    if platform.system() == "Windows":
        out = os.environ["USERPROFILE"]
    else:
        out = os.path.expanduser("~")
    return out
