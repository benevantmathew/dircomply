@echo off
setlocal
@REM ############################################################################## got config variables from env_config file
call "%~dp0env_config.bat"
@REM ##############################################################################
@REM get script file dir6
set script_dir=%~dp0
@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%
@REM ##############################################################################
@REM set root dir
set root_dir=%script_dir%/..
@REM cd to root dir
cd %root_dir%
@REM ##############################################################################
@REM get current dir path
set "folder=%cd%"
@REM get the dir name alone
for %%A in ("%folder%") do set "folder=%%~nxA"
@REM set the env name
set "name=%folder%-py%python_version%-env"
@REM ##############################################################################
@REM check if env already exist
if exist "%userprofile%\envs\%name%" (
	echo Enabling venv
) else (
	echo No venv. Run local_setup first.
	pause
	exit /b 1
)
@REM ##############################################################################
@REM Set paths
set "venv_path=%userprofile%\envs\%name%\Scripts\activate.bat"
@REM ##############################################################################
@REM Start new command window with Python venv and Git in PATH
start cmd.exe /k "set PATH=%git_path%;%PATH%;%win32_path% & call %venv_path%"