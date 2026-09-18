@echo off
rem Extra stations for the development BAs: ISD-Lite observations, then the HRRR extraction for the
rem stations not yet extracted, then consolidation. Detached; each stage repeats until it exits cleanly.
rem Log: %TEMP%\multi.log
set PYTHONUNBUFFERED=1
set LOG=%TEMP%\multi.log
cd /d "%~dp0.."
echo START %DATE% %TIME% >> "%LOG%"
call :stage scripts\fetch_isd.py
call :stage scripts\extract_hrrr.py --start 2020-12-02 --end 2025-12-31 --init-hours 12 6 --stations data\hrrr_multi\stations_new.csv --out data\hrrr_multi
call :stage scripts\extract_hrrr.py --consolidate --out data\hrrr_multi
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
