@echo off
setlocal
@REM ############################################################################## PYTHON VERSION VERY IMPORTANT
set "python_version=312"
@REM ############################################################################## other variables
:: Get the user directory 
set "userdir=%userprofile%"
@REM ############################################################################## Activate local env
@REM get script file dir
set script_dir=%~dp0
@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%
@REM set root dir
set rootdir=%script_dir%/..
@REM cd to root dir
cd %rootdir%
@REM get dir name
set "folder=%cd%"
:: Get the user directory 
set "userdir=%userprofile%"
for %%A in ("%folder%") do set "folder=%%~nxA"
set "name=%folder%-py%python_version%-env"
if exist "%userdir%\envs\%name%" (
    echo Enabling venv
) else (
    echo No venv. Run local_setup first.
    exit /b 1
)
set "path=%userdir%\envs\%name%\Scripts\activate.bat"
start cmd.exe /k %path%