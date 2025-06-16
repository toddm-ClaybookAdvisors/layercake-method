# game.py
# Prompt 0012 — Modular Map Loading with Irregular Room Generation

import os
import sys
import shutil
from mapgen import generate_map, MAP_WIDTH, MAP_HEIGHT, WALKABLE_TILES

PLAYER = '@'
VIEW_WIDTH = shutil.get_terminal_size((80, 24)).columns
VIEW_HEIGHT = shutil.get_terminal_size((80, 24)).lines - 2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    except ImportError:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def draw_map(game_map, px, py):
    top = max(0, min(py - VIEW_HEIGHT // 2, MAP_HEIGHT - VIEW_HEIGHT))
    left = max(0, min(px - VIEW_WIDTH // 2, MAP_WIDTH - VIEW_WIDTH))
    for y in range(top, top + VIEW_HEIGHT):
        row = ''
        for x in range(left, left + VIEW_WIDTH):
            row += PLAYER if (x == px and y == py) else game_map[y][x]
        print(row)

def update_position(game_map, px, py, key):
    dx = {'a': -1, 'd': 1}.get(key, 0)
    dy = {'w': -1, 's': 1}.get(key, 0)
    nx, ny = px + dx, py + dy
    if 0 <= nx < MAP_WIDTH and 0 <= ny < MAP_HEIGHT:
        if game_map[ny][nx] in WALKABLE_TILES:
            return nx, ny
    return px, py

def game_loop():
    game_map, (player_x, player_y) = generate_map()
    while True:
        clear_screen()
        draw_map(game_map, player_x, player_y)
        print("Use WASD to move, 'q' to quit.")
        key = get_key()
        if key == 'q':
            break
        player_x, player_y = update_position(game_map, player_x, player_y, key)

if __name__ == "__main__":
    game_loop()
