# 📁 dircomply - Folder Comparison Tool

`dircomply` is a lightweight tool to compare files between two directories.It highlights files that differ and those that are unique to each folder.Supports both CLI mode and GUI mode for ease of use.

## ✅ Features

- Compare files between two folders
- Detect differences in file contents
- List unique files in each folder
- Supported filetypes are listed later
- Override or append compare extensions and skipped directories from CLI
- Configure GUI font size/zoom for high-DPI monitors
- GUI mode for interactive comparison
- CLI mode for quick terminal use

## 💾 Installation

Install dircomply using pip:

```sh
pip install dircomply
```

## 🧪 Example Usage

Compare two folders via CLI:

```sh
dircomply /path/to/folder1 /path/to/folder2
```

Append one skipped directory and one content extension to the JSON defaults:

```sh
dircomply /path/to/folder1 /path/to/folder2 --append_skip_dir dist --append_content_ext .toml
```

Overwrite skipped directories and content extensions from the JSON defaults:

```sh
dircomply /path/to/folder1 /path/to/folder2 --skip_dir .git,build --content_ext .py --content_ext .json
```

Launch GUI mode:

```sh
dircomply
```

Launch GUI mode with temporary larger text/zoom:

```sh
dircomply --font_size 16 --result_font_size 16 --zoom 1.5
```

Launch GUI mode with light theme for one run:

```sh
dircomply --theme light
```

Show version info:

```sh
dircomply --version
```

Display author details:

```sh
dircomply --author
```

## 📌 Supported CLI Options

Option Description
--help, -h Show help message and exit
--version, -v Show version number and exit
--author, -a Show author name and exit
--email, -e Show author email and exit
--content_ext VALUE Overwrite JSON content_extensions
--append_content_ext VALUE Append to JSON content_extensions
--existence_ext VALUE Overwrite JSON existence_extensions
--append_existence_ext VALUE Append to JSON existence_extensions
--skip_dir VALUE Overwrite JSON skip_dirs
--append_skip_dir VALUE Append to JSON skip_dirs
--font_size VALUE Override GUI label/input/button font size
--result_font_size VALUE Override result popup text size
--zoom VALUE Override Tk scaling for high-DPI monitors
--theme {dark,light} Override GUI theme for this run

`VALUE` can be comma-separated or the flag can be repeated.
`--existance_ext` and `--append_existance_ext` are also accepted as aliases.
If no arguments are passed, GUI mode will be launched.

## 🔍 GUI Text Size / Zoom

The GUI reads user settings from:

```sh
~/.config/dircomply/settings.json
```

Example for a 2K/high-DPI monitor:

```json
{
    "ui": {
        "font_family": "Arial",
        "font_size": 16,
        "result_font_size": 16,
        "tk_scaling": 1.5,
        "window_width": 750,
        "window_height": 430,
        "popup_width": 950,
        "popup_height": 700,
        "theme": "dark"
    }
}
```

`tk_scaling` zooms the whole Tkinter UI. `font_size` and `result_font_size` control the text size. `theme` supports `dark` and `light`; dark is the default.

## 🔎 What Gets Compared?

dircomply compares only files with the following extensions:
```
        ".txt", ".py", ".bat", ".html", ".ts",".json",".scss",".tcl",".md",
        ".yaml",".yml",".ini",".in",".sh",".gitignore"
```

Also check below files on existence check rather than the content difference check.
```
        ".xlsx", ".csv", ".docx",
        ".png",".jpeg",".jpg",".ods",
        ".pdf", ".ico"
```

The default skipped directories are:
```
        ".git", ".venv", "nodemodules", ".vscode", "__pycache__", "build"
```

All other file types are ignored during the comparison.
