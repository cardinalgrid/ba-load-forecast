@echo off
rem Phase C run, detached: the groups given as arguments (default: single sentinel long).
rem Rows go to a local folder; the report to the repository. Repeated until it exits cleanly.
rem Log: %TEMP%\phase_c.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\phase_c.log
set REPO=%~dp0..
set GROUPS=%*
if "%GROUPS%"=="" set GROUPS=single sentinel long
echo START %DATE% %TIME% groups %GROUPS% >> "%LOG%"
set /a TRIES=0
:again
set /a TRIES+=1
cd /d "%REPO%"
python scripts\run_phase_c.py --groups %GROUPS% >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 50 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
echo ALL_DONE >> "%LOG%"
exit /b 0
