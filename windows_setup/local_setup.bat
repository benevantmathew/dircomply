@echo off
setlocal
echo =================================
echo Welcome to setup. This setup will create local virtual env
echo And then it install required python libraries from req.txt file in current directory
echo you can rerun this without any issue
@REM ############################################################################## got config variables from env_config file
call "%~dp0env_config.bat"
echo Using Python %python_version%
@REM ############################################################################## Python exe
if exist "%userprofile%\AppData\Local\Programs\Python\Python%python_version%\python.exe" (
	set python_exe="%userprofile%\AppData\Local\Programs\Python\Python%python_version%\python.exe"
) else (
	if exist "C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python%python_version%_64\python.exe" (
		set python_exe="C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python%python_version%_64\python.exe"
	) else (
		exit
	)
)
@REM ##############################################################################
@REM get script file dir
set script_dir=%~dp0
@REM Remove trailing backslash
if "%script_dir:~-1%"=="\" set script_dir=%script_dir:~0,-1%
@REM ##############################################################################
@REM set root dir
set root_dir=%script_dir%/..
@REM cd to root dir
cd %root_dir%
@REM ############################################ create envs folder if not exist
set envs_path=%userprofile%\envs
if not exist "%envs_path%" (
	mkdir "%envs_path%"
) 
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
	echo "%userprofile%\envs\%name%" folder exists
) else (
	echo Creating envs
	%python_exe% -m venv "%userprofile%\envs\%name%"
)
@REM ##############################################################################s
call %userprofile%\envs\%name%\Scripts\activate
python -m pip install --upgrade pip
@REM ##############################################################################
deactivate
pause