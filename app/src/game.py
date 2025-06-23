"""
game.py

Main game loop and state management. Orchestrates player, adversary, renderer, and input.
"""

import os
import sys
import time
import json
from mapgen import generate_map, place_entity
from entities import Player, Adversary
from renderer import Renderer
from utils import get_terminal_size, is_open_tile, is_floor, load_config

if os.name == "nt":
    import msvcrt
else:
    import termios
    import tty

class Game:
    def __init__(self, config):
        map_width = config["map_width"]
        map_height = config["map_height"]
        map_config = config.get("map_config", {})
        self.map, (px, py), self.exit_pos = generate_map(map_width, map_height, map_config)
        self.layer = config["LAYER"]
        self.player = Player(px, py)
        self.messages = []
        self.running = True
        self.last_frame_time = time.time()
        self.fps = 0.0
        self.tick = 0

        # FOG OF WAR: tracks which tiles have been seen
        self.seen = [[False for _ in range(map_width)] for _ in range(map_height)]
        self._reveal_visible_area()

        # Extract floor tile from config for safe adversary placement
        floor_tile = map_config.get("tileset", {}).get("floor", ".")
        occupied = {(px, py)}
        ax, ay = place_entity(self.map, occupied, floor_tile)
        self.adversary = Adversary(ax, ay)
        self.player_slow_counter = 0

        self.viewport_width, self.viewport_height = self._get_dynamic_viewport_size()
        self.renderer = Renderer(config)

    def _get_dynamic_viewport_size(self):
        term_w, term_h = get_terminal_size()
        reserved_top = 1
        reserved_bottom = 3
        reserved_input = 1
        available_h = max(term_h - reserved_top - reserved_bottom - reserved_input, 1)
        vp_w = min(term_w, len(self.map[0]))
        vp_h = min(available_h, len(self.map))
        return vp_w, vp_h

    def run(self):
        while self.running:
            frame_start = time.time()
            self.renderer.render(self, self.player, self.adversary, self.exit_pos)
            command = self._getch()
            moved = self._handle_input(command)
            player_on_red_trail = (self.player.x, self.player.y) in self.adversary.trail
            if player_on_red_trail:
                if self.player_slow_counter == 0 and moved:
                    self.player_slow_counter = 1
                    self._add_message("You are slowed by the adversary's trail!")
                elif self.player_slow_counter > 0:
                    self.player_slow_counter -= 1
                    moved = False
                    self._add_message("You are slowed by the adversary's trail!")
            else:
                self.player_slow_counter = 0
            if moved:
                self.player.trail.add((self.player.x, self.player.y))
                self.player.explored.add((self.player.x, self.player.y))
            self._reveal_visible_area()

            self.adversary.move(self, self.player.trail, (self.player.x, self.player.y), is_floor, self._add_message)

            if (self.adversary.x, self.adversary.y) == (self.player.x, self.player.y):
                self._add_message("You lose! The adversary caught you!")
                self.renderer.render(self, self.player, self.adversary, self.exit_pos)
                break

            if (self.player.x, self.player.y) == self.exit_pos:
                self._add_message("You found the exit! Congratulations!")
                self.renderer.render(self, self.player, self.adversary, self.exit_pos)
                break

            self.tick += 1
            frame_end = time.time()
            self._update_fps(frame_end - frame_start)

    def _update_fps(self, frame_duration):
        self.fps = 1.0 / frame_duration if frame_duration > 0 else 0.0

    def _reveal_visible_area(self):
        px, py = self.player.x, self.player.y
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                x = px + dx
                y = py + dy
                if 0 <= y < len(self.map) and 0 <= x < len(self.map[0]):
                    self.seen[y][x] = True

    def _getch(self):
        if os.name == "nt":
            ch = msvcrt.getch()
            try:
                return ch.decode("utf-8")
            except Exception:
                return ""
        else:
            fd = sys.stdin.fileno()
            import termios
            import tty
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

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
            print("Are you sure you want to quit? (y/N)", end=' ', flush=True)
            confirm = self._getch()
            print(confirm)
            if confirm in ("y", "Y"):
                self.running = False
                print("Goodbye!")
                return False
            else:
                self._add_message("Quit canceled.")
                return False
        else:
            self._add_message("Invalid input! Use W/A/S/D to move, Q to quit.")
            return False
        moved = self.player.move(dx, dy, self.map, is_open_tile)
        if moved:
            self.tick += 1
        else:
            self._add_message("You can't walk there.")
        return moved

    def _add_message(self, msg):
        self.messages.append(msg)

def main():
    config = load_config()
    game = Game(config)
    game.run()

if __name__ == "__main__":
    main()
