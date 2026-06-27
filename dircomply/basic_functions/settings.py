"""
settings.py

Author: Benevant Mathew
Date: 2026-06-27
"""
import json

DEFAULT_UI_SETTINGS = {
    "font_family": "Arial",
    "font_size": 14,
    "result_font_size": 14,
    "tk_scaling": 1.25,
    "window_width": 650,
    "window_height": 360,
    "popup_width": 850,
    "popup_height": 600,
}


def _positive_int(value, default_value):
    """
    Convert config values to positive int with fallback.
    """
    try:
        int_value = int(value)
    except (TypeError, ValueError):
        return default_value
    return int_value if int_value > 0 else default_value


def _positive_float(value, default_value):
    """
    Convert config values to positive float with fallback.
    """
    try:
        float_value = float(value)
    except (TypeError, ValueError):
        return default_value
    return float_value if float_value > 0 else default_value


def load_ui_settings(settings_filepath, overrides=None):
    """
    Load UI settings from settings.json and apply optional CLI overrides.
    """
    settings = DEFAULT_UI_SETTINGS.copy()

    try:
        with open(settings_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        data = {}

    if isinstance(data, dict) and isinstance(data.get("ui"), dict):
        settings.update(data["ui"])

    for key, value in (overrides or {}).items():
        if value is not None:
            settings[key] = value

    settings["font_family"] = str(settings.get("font_family") or DEFAULT_UI_SETTINGS["font_family"])
    for key in [
            "font_size",
            "result_font_size",
            "window_width",
            "window_height",
            "popup_width",
            "popup_height"
        ]:
        settings[key] = _positive_int(settings.get(key), DEFAULT_UI_SETTINGS[key])
    settings["tk_scaling"] = _positive_float(
        settings.get("tk_scaling"),
        DEFAULT_UI_SETTINGS["tk_scaling"]
    )

    return settings
