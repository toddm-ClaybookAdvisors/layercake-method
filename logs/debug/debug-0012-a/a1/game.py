# game.py — debug-0012-a1 (fixed import structure)
# Standalone version assuming mapgen.py is in the same folder

import os
import sys
import shutil
import mapgen

PLAYER = '@'

def get_terminal_size():
    size = shutil.get_terminal_size((100, 40))
    return size.columns, size.lines - 2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    except ImportError:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1).lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def draw_map(game_map, px, py, view_w, view_h):
    map_h = len(game_map)
    map_w = len(game_map[0])
    top = max(0, min(py - view_h // 2, map_h - view_h))
    left = max(0, min(px - view_w // 2, map_w - view_w))
    for y in range(top, top + view_h):
        row = ''
        for x in range(left, left + view_w):
            row += PLAYER if (x == px and y == py) else game_map[y][x]
        print(row)

def update_position(game_map, px, py, key):
    dx = {'a': -1, 'd': 1}.get(key, 0)
    dy = {'w': -1, 's': 1}.get(key, 0)
    nx, ny = px + dx, py + dy
    if 0 <= ny < len(game_map) and 0 <= nx < len(game_map[0]):
        if game_map[ny][nx] in mapgen.WALKABLE_TILES:
            return nx, ny
    return px, py

def game_loop():
    view_w, view_h = get_terminal_size()
    game_map, (px, py) = mapgen.generate_map(view_w, view_h)
    while True:
        clear_screen()
        draw_map(game_map, px, py, view_w, view_h)
        print("Use WASD to move. Press 'q' to quit.")
        key = get_key()
        if key == 'q':
            break
        px, py = update_position(game_map, px, py, key)

if __name__ == "__main__":
    game_loop()
