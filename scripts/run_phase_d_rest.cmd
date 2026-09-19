@echo off
rem The phase D groups that follow the base group, as one detached job with its own log
rem (Windows locks a log file that another job is already appending to). Log: %TEMP%\phase_d_rest.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\phase_d_rest.log
set REPO=%~dp0..
set GROUPS=extremes ensemble special quantiles
echo START %DATE% %TIME% groups %GROUPS% >> "%LOG%"
set /a TRIES=0
:again
set /a TRIES+=1
cd /d "%REPO%"
python scripts\run_phase_d.py --groups %GROUPS% >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 50 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
echo ALL_DONE >> "%LOG%"
exit /b 0
