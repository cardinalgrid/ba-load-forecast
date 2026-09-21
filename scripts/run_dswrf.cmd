@echo off
rem Forecast surface short-wave radiation from the HRRR GRIB2 archive for the stations of ISO-NE, CAISO and FPL
rem (the same table as the cloud extraction). Detached; each stage repeats until it exits cleanly.
rem Usage: run_dswrf.cmd 12   or   run_dswrf.cmd 6  (one job per initialisation hour, each with its own log).
rem Log: %TEMP%\dswrf_<hour>.log
set PYTHONUNBUFFERED=1
set HOUR=%1
if "%HOUR%"=="" set HOUR=12
set LOG=%TEMP%\dswrf_%HOUR%.log
cd /d "%~dp0.."
echo START %DATE% %TIME% >> "%LOG%"
call :stage scripts\extract_dswrf.py --start 2020-12-02 --end 2022-12-31 --init-hours %HOUR% --stations data\cloud\stations.csv --out data\dswrf
rem consolidation runs by hand once both jobs are done: python scripts\extract_dswrf.py --consolidate --out data\dswrf
echo ALL_DONE >> "%LOG%"
exit /b 0

:stage
set /a TRIES=0
:again
set /a TRIES+=1
python %* >> "%LOG%" 2>&1
if %ERRORLEVEL% neq 0 (
    echo STAGE FAILED [%*] try %TRIES%, waiting 60 s >> "%LOG%"
    if %TRIES% geq 200 exit /b 1
    timeout /t 60 /nobreak > nul
    goto again
)
exit /b 0
