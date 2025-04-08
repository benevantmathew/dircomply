@echo off

@REM get script file dir
set script_dir=%~dp0
@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%

echo Cleaning build directories...

:: Run the clean.py script to remove old build artifacts
python %script_dir%\clean.py

echo Done!
