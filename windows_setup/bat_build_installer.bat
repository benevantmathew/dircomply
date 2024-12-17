:: batch script to build installer 
@echo off 
setlocal
@REM ############################################################################## PYTHON VERSION VERY IMPORTANT
set "python_version=312"
@REM ############################################################################## other variables
:: Get the user directory 
set "userdir=%userprofile%"
@REM ############################################################################## Activate local env
set build_workspace=..\build
set "folder=dircomply"
@REM ############################################
@REM get version no
set /p version="Enter version no: "
@REM #####################################################################################
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
@REM #####################################################################################
echo "running pyinstaller....."
pyinstaller --clean main.spec
@REM #####################################################################################
echo "copy installer file....."
@REM #copy installer file
set source_path=.\dist\main.exe
set dest_path=..\releases\v%version%\repo_compare_v%version%.exe
@REM create required directories
if not exist "..\releases" (
    mkdir "..\releases"
)
if not exist "..\releases\v%version%" (
    mkdir "..\releases\v%version%"
)
copy /y "%source_path%" "%dest_path%"
@REM #####################################################################################
pause