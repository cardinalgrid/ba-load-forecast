@echo off
rem Forecast total cloud cover from the HRRR archive for the stations of the BAs where behind-the-meter solar
rem matters (ISO-NE, CAISO, FPL). Detached; each stage repeats until it exits cleanly. Log: %TEMP%\cloud.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\cloud.log
cd /d "%~dp0.."
echo START %DATE% %TIME% >> "%LOG%"
call :stage scripts\extract_hrrr.py --field cloud_pct --start 2020-12-02 --end 2025-12-31 --init-hours 12 6 --stations data\cloud\stations.csv --out data\cloud
call :stage scripts\extract_hrrr.py --consolidate --out data\cloud
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
