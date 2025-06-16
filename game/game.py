# Prompt 0009: Replace Random Obstacles with Room-and-Hallway Structure
# Generates structured rooms and hallways instead of random noise.
# Rooms are placed in a grid pattern and connected with straight corridors.
# The player spawns at the center of the first room.

import os
import sys
import random

WIDTH = 100
HEIGHT = 100
ROOM_WIDTH = 15
ROOM_HEIGHT = 7
ROOM_ROWS = 4
ROOM_COLS = 4

game_map = [['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]
player_x, player_y = 0, 0

def carve_room(x, y, w, h):
    """Carves out a rectangular room by replacing wall tiles with floor tiles."""
    for i in range(y, y + h):
        for j in range(x, x + w):
            if 0 <= j < WIDTH and 0 <= i < HEIGHT:
                game_map[i][j] = '.'

def carve_hallway(x1, y1, x2, y2):
    """Carves out a horizontal then vertical hallway between two points."""
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if 0 <= x < WIDTH and 0 <= y1 < HEIGHT:
            game_map[y1][x] = '.'
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if 0 <= x2 < WIDTH and 0 <= y < HEIGHT:
            game_map[y][x2] = '.'

def generate_structured_map():
    """Creates a grid of rooms connected by hallways."""
    global player_x, player_y
    room_centers = []

    for row in range(ROOM_ROWS):
        for col in range(ROOM_COLS):
            x = col * (ROOM_WIDTH + 3) + 2
            y = row * (ROOM_HEIGHT + 3) + 2
            carve_room(x, y, ROOM_WIDTH, ROOM_HEIGHT)
            center_x = x + ROOM_WIDTH // 2
            center_y = y + ROOM_HEIGHT // 2
            room_centers.append((center_x, center_y))

    # Connect each room to the next with hallways
    for i in range(1, len(room_centers)):
        prev = room_centers[i - 1]
        curr = room_centers[i]
        carve_hallway(prev[0], prev[1], curr[0], curr[1])

    # Place player in the center of the first room
    player_x, player_y = room_centers[0]

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
            ch = sys.stdin.read(1)
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def draw_map():
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            row += '@' if (x == player_x and y == player_y) else game_map[y][x]
        print(row)

def update_position(move):
    global player_x, player_y
    new_x, new_y = player_x, player_y

    if move == 'w': new_y -= 1
    elif move == 's': new_y += 1
    elif move == 'a': new_x -= 1
    elif move == 'd': new_x += 1

    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        if game_map[new_y][new_x] == '.':
            player_x, player_y = new_x, new_y

def game_loop():
    while True:
        clear_screen()
        draw_map()
        print("Use WASD to move. Press 'q' to quit.")
        move = get_key()
        if move == 'q':
            break
        update_position(move)

if __name__ == "__main__":
    generate_structured_map()
    game_loop()
