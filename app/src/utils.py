"""
utils.py

Utility functions and project-wide constants.
"""

import os
import re
import sys
import json
import logging

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
        logging.debug("Failed to determine terminal size; using default 80x24.")
        return 80, 24

def is_open_tile(game_map, x, y):
    result = 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] in ('.', '>')
    return result

def is_floor(game_map, x, y):
    result = 0 <= y < len(game_map) and 0 <= x < len(game_map[0]) and game_map[y][x] == '.'
    return result

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
        cleaned = {k: strip_json_comments(v, comment_prefix)
                for k, v in obj.items() if not k.startswith(comment_prefix)}
        logging.debug(f"Stripped comments from dict: {set(obj) - set(cleaned)}")
        return cleaned
    elif isinstance(obj, list):
        result = [strip_json_comments(item, comment_prefix) for item in obj]
        logging.debug(f"Stripped comments from list of length {len(obj)}")
        return result
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
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            raw_config = json.load(f)
            config = strip_json_comments(raw_config)
        logging.debug(f"Config loaded from {config_path}.")
        return config
    except FileNotFoundError:
        logging.error(f"Config file not found at {config_path}.")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Config file at {config_path} is invalid JSON: {e}")
        raise

def get_layer():
    """
    Returns the current LAYER from the loaded config.

    Returns:
        int: The current layer/version number.
    Raises:
        KeyError: If 'LAYER' is not present in the config.
    """
    config = load_config()
    layer = config['LAYER']
    logging.debug(f"Current LAYER from config: {layer}")
    return layer

def is_debug_mode():
    """
    Returns True if debug mode is enabled in config.json, False otherwise.
    """
    config = load_config()
    debug_flag = config.get('debug', False)
    logging.debug(f"Debug mode is {'on' if debug_flag else 'off'}.")
    return debug_flag

def setup_logger():
    """
    Configures the Python logger based on debug flag in config.json.
    Logs DEBUG messages to debug.log at the project root.
    Overwrites the log file at the start of each game run.
    """
    config = load_config()
    # Project root is two levels up from this file
    project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
    log_path = os.path.join(project_root, 'debug.log')

    logger = logging.getLogger()
    # Remove all handlers to avoid duplicates if re-initialized
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    handler = logging.FileHandler(log_path, mode='w')  # OVERWRITE log file each run
    formatter = logging.Formatter('[%(asctime)s] [%(module)s.%(funcName)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG if config.get('debug', False) else logging.WARNING)
    logging.debug("Logger initialized.")


# End of utils.py
