@echo off
rem Detached extraction of HRRR 2 m temperature for every station, in the order the study needs it:
rem 2024 first (verification), then the other years. Safe to relaunch: finished runs are skipped.
rem Each stage is repeated (after a minute) until it exits cleanly, so a network outage only delays it.
rem Log: %TEMP%\hrrr_extract.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\hrrr_extract.log
cd /d "%~dp0.."
echo START %DATE% %TIME% >> "%LOG%"
call :stage --start 2024-01-01 --end 2024-12-31 --init-hours 12 6
call :stage --start 2021-01-01 --end 2023-12-31 --init-hours 12 6
call :stage --start 2025-01-01 --end 2025-12-31 --init-hours 12 6
call :stage --start 2020-12-02 --end 2020-12-31 --init-hours 12 6
call :stage --consolidate
echo ALL_DONE >> "%LOG%"
exit /b 0

:stage
set /a TRIES=0
:again
set /a TRIES+=1
python scripts\extract_hrrr.py %* >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED [%*] try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 200 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
exit /b 0
