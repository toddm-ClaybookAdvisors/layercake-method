# Prompt 0010: Finalize Scrollable Viewport for Structured Map
# Implements scrollable viewport with edge clamping
# Restores detailed explanatory comments to all core functions

import os
import sys
import shutil
import random

# Dynamically size the map and viewport based on the terminal
term_size = shutil.get_terminal_size((80, 24))
MAP_WIDTH = term_size.columns
MAP_HEIGHT = term_size.lines - 2  # subtract 2 for command prompt lines
VIEW_WIDTH = MAP_WIDTH
VIEW_HEIGHT = MAP_HEIGHT

# Room layout parameters
ROOM_WIDTH = 12
ROOM_HEIGHT = 5
ROOM_ROWS = max(1, VIEW_HEIGHT // (ROOM_HEIGHT + 2))
ROOM_COLS = max(1, VIEW_WIDTH // (ROOM_WIDTH + 2))

# Game state variables
game_map = [['#' for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
player_x, player_y = 0, 0

def carve_room(x, y, w, h):
    """
    Carves a rectangular room into the game map by replacing '#' with '.'
    """
    for i in range(y, y + h):
        for j in range(x, x + w):
            if 0 <= j < MAP_WIDTH and 0 <= i < MAP_HEIGHT:
                game_map[i][j] = '.'

def carve_hallway(x1, y1, x2, y2):
    """
    Carves a horizontal then vertical hallway between two points.
    """
    for x in range(min(x1, x2), max(x1, x2) + 1):
        if 0 <= x < MAP_WIDTH and 0 <= y1 < MAP_HEIGHT:
            game_map[y1][x] = '.'
    for y in range(min(y1, y2), max(y1, y2) + 1):
        if 0 <= x2 < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
            game_map[y][x2] = '.'

def generate_structured_map():
    """
    Creates a grid of rooms connected by hallways.
    Spawns the player in the center of one of the middle rooms.
    """
    global player_x, player_y
    room_centers = []

    for row in range(ROOM_ROWS):
        for col in range(ROOM_COLS):
            x = col * (ROOM_WIDTH + 2) + 1
            y = row * (ROOM_HEIGHT + 2) + 1
            carve_room(x, y, ROOM_WIDTH, ROOM_HEIGHT)
            center_x = x + ROOM_WIDTH // 2
            center_y = y + ROOM_HEIGHT // 2
            room_centers.append((center_x, center_y))

    for i in range(1, len(room_centers)):
        carve_hallway(*room_centers[i - 1], *room_centers[i])

    # Player starts in the middle room
    player_x, player_y = room_centers[len(room_centers) // 2]

def clear_screen():
    """
    Clears the terminal screen between frames.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    """
    Captures a single character of input from the keyboard without requiring Enter.
    Uses msvcrt on Windows or termios/tty on Unix.
    """
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
    """
    Renders a viewport centered on the player, clamped to map boundaries.
    """
    top = max(0, min(player_y - VIEW_HEIGHT // 2, MAP_HEIGHT - VIEW_HEIGHT))
    left = max(0, min(player_x - VIEW_WIDTH // 2, MAP_WIDTH - VIEW_WIDTH))
    for y in range(top, top + VIEW_HEIGHT):
        row = ''
        for x in range(left, left + VIEW_WIDTH):
            row += '@' if x == player_x and y == player_y else game_map[y][x]
        print(row)

def update_position(move):
    """
    Updates the player's position on valid movement input (WASD).
    Ignores input if the move would lead to a wall or off the map.
    """
    global player_x, player_y
    new_x, new_y = player_x, player_y
    if move == 'w': new_y -= 1
    elif move == 's': new_y += 1
    elif move == 'a': new_x -= 1
    elif move == 'd': new_x += 1
    if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT:
        if game_map[new_y][new_x] == '.':
            player_x, player_y = new_x, new_y

def game_loop():
    """
    Main loop: renders the view, gets input, updates state.
    Terminates when 'q' is pressed.
    """
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
