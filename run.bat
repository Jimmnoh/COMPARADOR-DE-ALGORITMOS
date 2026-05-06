@echo off
title SortBench
echo.
echo  ╔══════════════════════════════════════╗
echo  ║   SortBench — Iniciando...           ║
echo  ║   Se abrira el navegador en breve    ║
echo  ╚══════════════════════════════════════╝
echo.
pip install flask --quiet 2>nul
python app.py
pause
