@echo off
SET PYINSTALLER=pyinstaller.exe
SET SCRIPT=.\pypdf-unlocker.py
SET ICON=icon.ico
SET OUTPUT=dist\pypdf-unlocker.exe

%PYINSTALLER% -F --icon=%ICON% --windowed %SCRIPT%

if %ERRORLEVEL% == 0 (
    echo Build successful.
) else (
    echo Build failed.
)

pause