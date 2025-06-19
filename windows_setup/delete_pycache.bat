@echo off
setlocal

@REM get script file dir
set script_dir=%~dp0

@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%

:: Define the root folder
set rootdir=%script_dir%/..

:: Find and delete all __pycache__ folders
for /d /r "%rootdir%" %%d in (__pycache__) do (
    echo Deleting %%d
    rd /s /q "%%d"
)

echo Cleanup complete.
exit /b 0
