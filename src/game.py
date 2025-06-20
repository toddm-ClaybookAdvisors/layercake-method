"""
game.py

Adds persistent fog of war: every map tile seen by the player (ever in the viewport) remains visible.
Unexplored tiles appear blank.
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

        # FOG OF WAR: tracks which tiles have been seen
        self.seen = [[False for _ in range(map_width)] for _ in range(map_height)]
        self._reveal_viewport()  # Reveal initial viewport

    def run(self):
        while self.running:
            frame_start = time.time()
            self._render()
            command = _getch()
            self._handle_input(command)
            self._reveal_viewport()  # Update fog after move
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

    def _reveal_viewport(self):
        """Mark all tiles currently in the viewport as seen."""
        px, py = self.player.x, self.player.y
        vw, vh = self.viewport_width, self.viewport_height
        rows, cols = len(self.map), len(self.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh
        for y in range(top, min(bottom, rows)):
            for x in range(left, min(right, cols)):
                self.seen[y][x] = True

    def _render(self, final=False):
        os.system("cls" if os.name == "nt" else "clear")

        term_w, term_h = _get_terminal_size()
        vp_w = self.viewport_width
        vp_h = self.viewport_height
        offset_x = max((term_w - vp_w) // 2, 0)
        offset_y = max((term_h - vp_h) // 2, 0)

        # Overlay
        overlay = f"{VERSION}   FPS: {int(self.fps)}"
        print(overlay.ljust(term_w)[:term_w])

        for _ in range(offset_y):
            print()

        # Draw persistent fog of war (full map, but only seen tiles or viewport)
        viewport = self._get_fog_viewport()

        for row in viewport:
            print(" " * offset_x + "".join(row))

        if self.messages or final:
            print()
            print("\n".join(self.messages[-3:]))

    def _get_fog_viewport(self):
        """Return the current viewport, showing seen tiles or blank for unseen."""
        px, py = self.player.x, self.player.y
        vw, vh = self.viewport_width, self.viewport_height
        rows, cols = len(self.map), len(self.map[0])
        left = max(0, min(px - vw // 2, cols - vw))
        top = max(0, min(py - vh // 2, rows - vh))
        right = left + vw
        bottom = top + vh

        out = []
        for y in range(top, min(bottom, rows)):
            line = []
            for x in range(left, min(right, cols)):
                if self.seen[y][x]:
                    # Show player if this is their position
                    if (x, y) == (self.player.x, self.player.y):
                        line.append('@')
                    else:
                        line.append(self.map[y][x])
                else:
                    line.append(' ')
            out.append(line)
        return out

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

def main():
    game = Game(MAP_WIDTH, MAP_HEIGHT, VIEWPORT_WIDTH, VIEWPORT_HEIGHT)
    game.run()

if __name__ == "__main__":
    main()
