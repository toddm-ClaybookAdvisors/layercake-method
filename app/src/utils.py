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

def strip_json_comments(obj, comment_prefix="_comment"):
    """
    Recursively remove all keys starting with the given prefix (default: '_comment')
    from a loaded JSON dictionary or list.

    Args:
        obj: The Python object parsed from JSON (dict, list, or primitive).
        comment_prefix: The key prefix used for comments to strip (default: '_comment').

    Returns:
        A new object with all comment keys removed.
    """
    if isinstance(obj, dict):
        return {k: strip_json_comments(v, comment_prefix)
                for k, v in obj.items() if not k.startswith(comment_prefix)}
    elif isinstance(obj, list):
        return [strip_json_comments(item, comment_prefix) for item in obj]
    else:
        return obj


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
        raw_config = json.load(f)
        config = strip_json_comments(raw_config)
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
