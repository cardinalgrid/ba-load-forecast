@echo off
rem Detached extraction of HRRR 2 m temperature for every station, in the order the study needs it:
rem 2024 first (verification), then the other years. Safe to relaunch: finished runs are skipped.
set PYTHONUNBUFFERED=1
cd /d "%~dp0.."
python scripts\extract_hrrr.py --start 2024-01-01 --end 2024-12-31 --init-hours 12 6
python scripts\extract_hrrr.py --start 2021-01-01 --end 2023-12-31 --init-hours 12 6
python scripts\extract_hrrr.py --start 2025-01-01 --end 2025-12-31 --init-hours 12 6
python scripts\extract_hrrr.py --start 2020-12-02 --end 2020-12-31 --init-hours 12 6
python scripts\extract_hrrr.py --consolidate
echo ALL_DONE
