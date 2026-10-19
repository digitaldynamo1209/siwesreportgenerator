@echo off
title Landmark University SIWES Report Generator
echo =======================================================
echo   Starting Landmark University SIWES Report Generator
echo   Opening web browser at http://localhost:8000...
echo =======================================================
cd /d "%~dp0"
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
)
start "" "http://localhost:8000"
python run.py
pause
