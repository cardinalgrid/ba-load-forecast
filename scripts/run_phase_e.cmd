@echo off
rem Phase E run, detached, one group per job so that each job has its own log (Windows locks a log
rem another job is appending to). Usage: run_phase_e.cmd recipe   or   run_phase_e.cmd intervals
rem Log: %TEMP%\phase_e_<group>.log
set PYTHONUNBUFFERED=1
set GROUP=%1
if "%GROUP%"=="" set GROUP=recipe
set LOG=%TEMP%\phase_e_%GROUP%.log
set REPO=%~dp0..
echo START %DATE% %TIME% group %GROUP% >> "%LOG%"
set /a TRIES=0
:again
set /a TRIES+=1
cd /d "%REPO%"
python scripts\run_phase_e.py --groups %GROUP% >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 50 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
echo ALL_DONE >> "%LOG%"
exit /b 0
