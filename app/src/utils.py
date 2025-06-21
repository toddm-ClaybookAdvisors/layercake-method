"""
utils.py

Utility functions and project-wide constants.
"""

import os
import re
import sys

def get_terminal_size():
    try:
        if os.name == 'nt':
            from shutil import get_terminal_size as gts
            size = gts()
            return size.columns, size.lines
        else:
            import fcntl, termios, struct
            h, w, _, _ = struct.unpack('HHHH',
                fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))
            return w, h
    except Exception:
        return 80, 24

def get_version():
    path = os.path.join(os.path.dirname(__file__), "../PROMPTS.md")
    try:
        with open(path) as f:
            text = f.read()
        matches = re.findall(r'## Prompt (\d+):', text)
        if matches:
            latest = max(int(n) for n in matches)
            return f"version 0.{latest + 1}"
    except Exception:
        pass
    return "version unknown"

def is_open_tile(game_map, x, y):
    return 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] in ('.', '>')

def is_floor(game_map, x, y):
    return 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] == '.'

