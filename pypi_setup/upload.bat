@echo off

@REM get script file dir
set script_dir=%~dp0
@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%
@REM set root dir
set rootdir=%script_dir%/..
@REM cd to root dir
cd %rootdir%

echo Cleaning build directories...

:: Run the clean.py script to remove old build artifacts
python pypi_setup\clean.py

echo Building distribution packages...
python setup.py sdist bdist_wheel

echo Uploading to PyPI...
twine upload dist/*

echo Done!
