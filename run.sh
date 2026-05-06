#!/bin/bash
echo ""
echo "  ╔══════════════════════════════════════╗"
echo "  ║   SortBench — Iniciando...           ║"
echo "  ║   Se abrirá el navegador en breve    ║"
echo "  ╚══════════════════════════════════════╝"
echo ""
pip install flask --quiet 2>/dev/null || pip3 install flask --quiet 2>/dev/null
python3 app.py
