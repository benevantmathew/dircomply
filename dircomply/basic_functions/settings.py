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
    "result_line_spacing": 6,
    "result_text_bold": True,
    "tk_scaling": 1.25,
    "window_width": 650,
    "window_height": 360,
    "popup_width": 850,
    "popup_height": 600,
    "theme": "dark",
}

THEME_COLORS = {
    "dark": {
        "background_color": "#1e1e1e",
        "foreground_color": "#f2f2f2",
        "input_background_color": "#2d2d2d",
        "input_foreground_color": "#ffffff",
        "button_background_color": "#3a3a3a",
        "button_foreground_color": "#ffffff",
        "accent_color": "#2563eb",
        "result_background_color": "#111827",
        "result_foreground_color": "#f9fafb",
        "scrollbar_background_color": "#2d2d2d",
    },
    "light": {
        "background_color": "#f4f4f5",
        "foreground_color": "#111827",
        "input_background_color": "#ffffff",
        "input_foreground_color": "#111827",
        "button_background_color": "#e5e7eb",
        "button_foreground_color": "#111827",
        "accent_color": "#bfdbfe",
        "result_background_color": "#ffffff",
        "result_foreground_color": "#111827",
        "scrollbar_background_color": "#e5e7eb",
    },
}

COLOR_KEYS = tuple(next(iter(THEME_COLORS.values())).keys())


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


def _normalize_theme(value):
    """
    Normalize theme name with dark fallback.
    """
    theme = str(value or DEFAULT_UI_SETTINGS["theme"]).strip().lower()
    return theme if theme in THEME_COLORS else DEFAULT_UI_SETTINGS["theme"]


def _bool_value(value, default_value):
    """
    Convert config values to bool with fallback.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized_value = value.strip().lower()
        if normalized_value in {"1", "true", "yes", "y", "on"}:
            return True
        if normalized_value in {"0", "false", "no", "n", "off"}:
            return False
    return default_value


def load_ui_settings(settings_filepath, overrides=None):
    """
    Load UI settings from settings.json and apply optional CLI overrides.
    """
    try:
        with open(settings_filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        data = {}

    file_settings = {}
    if isinstance(data, dict) and isinstance(data.get("ui"), dict):
        file_settings = data["ui"]

    theme = _normalize_theme(file_settings.get("theme", DEFAULT_UI_SETTINGS["theme"]))
    if overrides and overrides.get("theme") is not None:
        theme = _normalize_theme(overrides["theme"])

    settings = DEFAULT_UI_SETTINGS.copy()
    settings.update(THEME_COLORS[theme])
    settings.update(file_settings)

    for key, value in (overrides or {}).items():
        if value is not None:
            settings[key] = value

    settings["theme"] = _normalize_theme(settings.get("theme"))
    if settings["theme"] != theme:
        # Theme changed through an override after initial palette selection.
        explicit_colors = {
            key: settings[key]
            for key in COLOR_KEYS
            if key in file_settings or (overrides or {}).get(key) is not None
        }
        settings.update(THEME_COLORS[settings["theme"]])
        settings.update(explicit_colors)

    settings["font_family"] = str(settings.get("font_family") or DEFAULT_UI_SETTINGS["font_family"])
    for key in [
            "font_size",
            "result_font_size",
            "result_line_spacing",
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
    settings["result_text_bold"] = _bool_value(
        settings.get("result_text_bold"),
        DEFAULT_UI_SETTINGS["result_text_bold"]
    )

    for key in COLOR_KEYS:
        settings[key] = str(settings.get(key) or THEME_COLORS[settings["theme"]][key])

    return settings
