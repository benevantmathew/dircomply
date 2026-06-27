# Changelog
## Version 1.3.0 - 2026-06-27

- Added configurable result popup line spacing through `result_line_spacing` in settings.
- Added `--result_line_spacing` CLI override for one-run tuning.
- Added configurable bold result popup text through `result_text_bold` in settings.
- Added `--result_text_bold true|false` CLI override for one-run tuning.

## Version 1.2.2 - 2026-06-27

- Added dark/light GUI theme support with dark as the default.
- Added `theme` to `settings.json` and `--theme {dark,light}` CLI override.
- Styled main window, result popup, inputs, buttons, and scrollbars from theme colors.

## Version 1.2.1 - 2026-06-27

- Added GUI settings file support at `~/.config/dircomply/settings.json`.
- Added configurable GUI font size, result text size, Tk scaling, and window sizes.
- Added temporary CLI overrides: `--font_size`, `--result_font_size`, and `--zoom`.

## Version 1.2.0 - 2026-06-27

- Added CLI overwrite and append flags for content extensions, existence extensions, and skipped directories.
- Added comma-separated/repeated flag parsing and existence/existance aliases.

## Version 1.1.0 - 2026-05-09

- Runtime issue resolved from 1.1.0

## Version 1.1.0 - 2026-05-09

- Added LICENSE and MANIFEST.in
- Create first AUR Release

## Version 1.0.0 - 2025-11-15

- Added LICENSE and MANIFEST.in
- Create first AUR Release

## Version 0.9.0 - 2025-11-12

- Added existence check these extensions- ".pdf",
- Added content check these extensions- ".ini", ".in", ".sh", ".gitignore"

## Version 0.8.0 - 2025-09-21

- Added existence check these extensions- ".xlsx", ".csv", ".docx",".png", ".jpeg", ".jpg", ".ods"

## Version 0.7.0 - 2025-09-20

- Added file support on ".yaml", ".yml"

## Version 0.6.0 - 2025-06-19

- Added file support on ".md",".tcl"

## Version 0.5.0 - 2025-06-17

- Added file support on ".json", ".ts", ".scss" for angular dev.

## Version 0.4.0 - 2025-04-08

- Report shows both folder paths in top for quick reference.

## Version 0.3.0 - 2025-04-08

- Show Folder Paths dynamically in report.

## Version 0.2.0 - 2025-04-07

- Added sort feature in all output files list. (Path)
- Updated readme and changelog.
- Added compare on cli mode.

## Version 0.1 - 2024-12-18

- The app will compare two folders and show the difference in ".txt", ".py", ".bat", ".html" files in both repo.
- Along with app will display unique files for each repo.
