:: batch script to create spec file for weldeasy installer 
@echo off 
setlocal
@REM ############################################################################## PYTHON VERSION VERY IMPORTANT
set "python_version=312"
@REM ############################################################################## other variables
:: Get the user directory 
set "userdir=%userprofile%"
@REM ############################################
set build_workspace=..\build
set "folder=repo_compare"
@REM ############################################
if not exist "%build_workspace%" (
    mkdir "%build_workspace%"
) 
cd %build_workspace%
for %%A in ("%folder%") do set "folder=%%~nxA"
set "name=%folder%-py%python_version%-env"
if exist "%userdir%\envs\%name%" (
    echo Enabling venv.....
) else (
    echo No local environment.
    exit /b 1
)
set "path=%userdir%\envs\%name%\Scripts\activate.bat"
call %path%
@REM ############################################
echo "running pyinstaller....."
pyi-makespec "..\main.py" --onefile -F --noconsole --add-data "..\main.py;."
pause