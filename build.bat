@echo off
python -m PyInstaller --onefile --windowed --name ProjectLauncher main.py
copy projects.json dist\
copy .env dist\
echo Listo! Ejecutable en dist\ProjectLauncher.exe