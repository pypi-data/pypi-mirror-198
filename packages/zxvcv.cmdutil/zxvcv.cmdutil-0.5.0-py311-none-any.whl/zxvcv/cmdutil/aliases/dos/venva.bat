@echo off
SETLOCAL

IF "%1"=="--help" (
    echo Activate python virtual env
    echo usage venva [--help] name
    echo.
    echo arguments:
    echo   --help      show brief help message
    echo   name        anme of python virtual environment to activate
    goto end_fun
)

ENDLOCAL

CALL :GETPARENT PARENT
IF /I "%PARENT%" == "powershell" GOTO :ispowershell
IF /I "%PARENT%" == "pwsh" GOTO :ispowershell

GOTO :isbat

GOTO :EOF


:GETPARENT
SET "PSCMD=$ppid=$pid;while($i++ -lt 3 -and ($ppid=(Get-CimInstance Win32_Process -Filter ('ProcessID='+$ppid)).ParentProcessId)) {}; (Get-Process -EA Ignore -ID $ppid).Name"
for /f "tokens=*" %%i in ('powershell -noprofile -command "%PSCMD%"') do SET %1=%%i
GOTO :EOF

:isbat
C:\PythonVenv\%1\Scripts\activate
GOTO :EOF

:ispowershell
Powershell.exe -ExecutionPolicy Bypass -noexit -Command ". C:\PythonVenv\%1\Scripts\Activate.ps1"
GOTO :EOF
