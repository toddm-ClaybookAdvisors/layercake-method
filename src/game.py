"""
game.py

Main game loop and interface for the LLM-driven 2D adventure game.

- Reads map/viewport size from config.json (project root)
- Viewport is always a window into a much larger map (default 100x100)
- Real-time, single-key movement (no ENTER required)
- Overlay in upper-left corner: version 0.<next commit>   FPS: <current_fps>
- Dynamic version number (from PROMPTS.md + 1)
"""

import os
import sys
import time
import re
import json
from mapgen import generate_map

if os.name == "nt":
    import msvcrt
else:
    import termios
    import tty

# --- Configuration Loading ---

def load_config():
    """Loads configuration from ../config.json, falling back to defaults."""
    default = {
        "map_width": 100,
        "map_height": 100,
        "viewport_width": 40,
        "viewport_height": 20
    }
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    try:
        with open(config_path) as f:
            user_config = json.load(f)
        for k in default:
            if k not in user_config:
                user_config[k] = default[k]
        return user_config
    except Exception:
        return default

CONFIG = load_config()
MAP_WIDTH = CONFIG["map_width"]
MAP_HEIGHT = CONFIG["map_height"]
VIEWPORT_WIDTH = CONFIG["viewport_width"]
VIEWPORT_HEIGHT = CONFIG["viewport_height"]

# --- Dynamic Version ---

def _get_version():
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

VERSION = _get_version()

# --- Player and Game Classes ---

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, game_map):
        nx, ny = self.x + dx, self.y + dy
        if _is_open_tile(game_map, nx, ny):
            self.x, self.y = nx, ny
            return True
        return False

class Game:
    def __init__(self, map_width, map_height, viewport_width, viewport_height):
        self.map, (px, py), self.exit_pos = generate_map(map_width, map_height)
        self.player = Player(px, py)
        self.messages = []
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.running = True
        self.last_frame_time = time.time()
        self.fps = 0.0

    def run(self):
        while self.running:
            frame_start = time.time()
            self._render()
            command = _getch()
            self._handle_input(command)
            if (self.player.x, self.player.y) == self.exit_pos:
                self._add_message("You found the exit! Congratulations!")
                self._render(final=True)
                break
            frame_end = time.time()
            self._update_fps(frame_end - frame_start)

    def _update_fps(self, frame_duration):
        if frame_duration > 0:
            self.fps = 1.0 / frame_duration
        else:
            self.fps = 0.0

    def _render(self, final=False):
        os.system("cls" if os.name == "nt" else "clear")

        term_w, term_h = _get_terminal_size()
        vp_w = self.viewport_width
        vp_h = self.viewport_height
        offset_x = max((term_w - vp_w) // 2, 0)
        offset_y = max((term_h - vp_h) // 2, 0)

        viewport = _get_viewport(
            self.map, self.player.x, self.player.y, vp_w, vp_h
        )

        overlay = f"{VERSION}   FPS: {int(self.fps)}"
        print(overlay.ljust(term_w)[:term_w])

        for _ in range(offset_y):
            print()

        for row in viewport:
            line = "".join(row)
            print(" " * offset_x + line)

        if self.messages or final:
            print()
            print("\n".join(self.messages[-3:]))

    def _handle_input(self, command):
        dx, dy = 0, 0
        if command in ("w", "W"):
            dy = -1
        elif command in ("s", "S"):
            dy = 1
        elif command in ("a", "A"):
            dx = -1
        elif command in ("d", "D"):
            dx = 1
        elif command in ("q", "Q"):
            self.running = False
            print("Goodbye!")
            return
        else:
            self._add_message("Invalid input! Use W/A/S/D to move, Q to quit.")
            return
        moved = self.player.move(dx, dy, self.map)
        if not moved:
            self._add_message("You can't walk there.")

    def _add_message(self, msg):
        self.messages.append(msg)

# --- Core Helpers ---

def _is_open_tile(game_map, x, y):
    if 0 <= y < len(game_map) and 0 <= x < len(game_map[0]):
        return game_map[y][x] in ('.', '>')
    return False

def _get_viewport(game_map, px, py, vw, vh):
    rows, cols = len(game_map), len(game_map[0])
    left = max(0, min(px - vw // 2, cols - vw))
    top = max(0, min(py - vh // 2, rows - vh))
    right = left + vw
    bottom = top + vh
    view = [list(row[left:right]) for row in game_map[top:bottom]]
    vx, vy = px - left, py - top
    if 0 <= vy < len(view) and 0 <= vx < len(view[0]):
        view[vy][vx] = '@'
    return view

def _get_terminal_size():
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

def _getch():
    if os.name == "nt":
        ch = msvcrt.getch()
        try:
            return ch.decode("utf-8")
        except Exception:
            return ""
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

# --- Entry Point ---

def main():
    game = Game(MAP_WIDTH, MAP_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
