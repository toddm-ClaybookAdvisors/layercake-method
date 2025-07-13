"""
utils.py

Utility functions and project-wide constants using config-driven tile definitions.
"""

import os
import re
import sys
import json
import logging

def get_terminal_size():
    """
    Get the current terminal size in columns and rows.
    
    Returns:
        Tuple (width, height) of terminal dimensions
    """
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
    """
    Check if a tile is open for movement (floor or exit).
    Uses config-driven tile definitions.
    
    Args:
        game_map: The game map (row-major: map[y][x])
        x, y: Coordinates to check
        
    Returns:
        True if tile allows movement, False otherwise
    """
    if not (0 <= y < len(game_map) and 0 <= x < len(game_map[0])):
        return False
        
    config = load_config()
    floor_tile = config["map_config"]["tileset"]["floor"]
    exit_tile = config["characters"]["exit"]
    
    tile = game_map[y][x]
    return tile in (floor_tile, exit_tile)

def is_floor(game_map, x, y):
    """
    Check if a tile is a floor tile.
    Uses config-driven tile definition.
    
    Args:
        game_map: The game map (row-major: map[y][x])
        x, y: Coordinates to check
        
    Returns:
        True if tile is a floor, False otherwise
    """
    if not (0 <= y < len(game_map) and 0 <= x < len(game_map[0])):
        return False
        
    config = load_config()
    floor_tile = config["map_config"]["tileset"]["floor"]
    
    return game_map[y][x] == floor_tile

def get_tile_types():
    """
    Get all tile type definitions from config.
    
    Returns:
        Dictionary containing tile type mappings
    """
    config = load_config()
    return {
        'wall': config["map_config"]["tileset"]["wall"],
        'floor': config["map_config"]["tileset"]["floor"],
        'player': config["characters"]["player"],
        'adversary': config["characters"]["adversary"],
        'trap': config["characters"]["trap"],
        'exit': config["characters"]["exit"],
        'trail_player': config["characters"]["trail_player"],
        'trail_adversary': config["characters"]["trail_adversary"],
        'alert_marker': config["characters"]["alert_marker"],
        'empty': config["characters"]["empty"]
    }

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
        dict: The loaded configuration with comments stripped.
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
    
    Returns:
        bool: True if debug mode is enabled
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

def validate_config():
    """
    Validate that the loaded config contains all required keys.
    
    Returns:
        bool: True if config is valid
    Raises:
        KeyError: If required config keys are missing
        ValueError: If config values are invalid
    """
    config = load_config()
    
    # Required top-level keys
    required_keys = ['LAYER', 'debug', 'entities', 'gameplay', 'characters', 'colors', 'ui', 'input', 'map_config']
    
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Required config key '{key}' is missing")
    
    # Validate tileset
    tileset = config['map_config'].get('tileset', {})
    if 'wall' not in tileset or 'floor' not in tileset:
        raise ValueError("Config tileset must contain 'wall' and 'floor' keys")
    
    # Validate character mappings
    required_chars = ['player', 'adversary', 'trap', 'exit', 'trail_player', 'trail_adversary', 'alert_marker', 'empty']
    characters = config.get('characters', {})
    
    for char_key in required_chars:
        if char_key not in characters:
            raise KeyError(f"Required character mapping '{char_key}' is missing")
    
    logging.debug("Config validation passed.")
    return True

# End of utils.py