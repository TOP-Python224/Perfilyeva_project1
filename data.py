"""Дополнительный модуль: глобальные переменные и константы."""

from pathlib import Path
from sys import path

# глобальные константы
APP_TITLE = "КРЕСТИКИ-НОЛИКИ"
PROMPT = ' > '

script_dir = Path(path[0])
players_ini_path = script_dir / 'players.ini'
saves_ini_path = script_dir / 'saves.ini'

# глобальные переменные данных
STATS = {}
SAVES = {}