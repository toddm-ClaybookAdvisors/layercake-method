"""
utils.py

Utility functions and project-wide constants.
"""

import os
import re
import sys
import json

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

def is_open_tile(game_map, x, y):
    return 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] in ('.', '>')

def is_floor(game_map, x, y):
    return 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] == '.'

def load_config():
    """
    Loads the configuration from 'app/config.json', using a path
    relative to the project root directory (where chat-boot.md and README.md live).

    Returns:
        dict: The loaded configuration.
    Raises:
        FileNotFoundError: If config.json is not found at the expected path.
        json.JSONDecodeError: If config.json contains invalid JSON.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    config_path = os.path.join(project_root, 'app', 'config.json')

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config

def get_layer():
    """
    Returns the current LAYER from the loaded config.

    Returns:
        int: The current layer/version number.
    Raises:
        KeyError: If 'LAYER' is not present in the config.
    """
    config = load_config()
    return config['LAYER']
