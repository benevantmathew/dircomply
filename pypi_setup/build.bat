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

:: Find the latest .whl file in the dist folder
for /f %%i in ('dir /b /o-d dist\*.whl') do set latest_whl=dist\%%i & goto install

:install
if not exist "%latest_whl%" (
    echo ERROR: No wheel file found in dist directory!
    exit /b 1
)

echo Installing package locally...
pip install --force-reinstall "%latest_whl%"

echo Done!
