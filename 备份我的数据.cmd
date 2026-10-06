@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
"%~dp0runtime\python.exe" launcher.py --backup
echo.
pause
