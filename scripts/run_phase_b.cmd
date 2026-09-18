@echo off
rem Phase B run, detached. Rows go to a local folder (not the synced drive); the report to the repository.
rem Repeated until it exits cleanly. Log: %TEMP%\phase_b.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\phase_b.log
set REPO=%~dp0..
echo START %DATE% %TIME% >> "%LOG%"
set /a TRIES=0
:again
set /a TRIES+=1
cd /d "%REPO%"
python scripts\run_phase_b.py >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 50 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
echo ALL_DONE >> "%LOG%"
exit /b 0
