# Prompt 0008: Add Static Obstacles and Expand Map to 100×100
# Adds impassable tiles ('#') and increases map dimensions to 100x100.
# Player movement and rendering logic are updated accordingly.
# The obstacle map is generated once at startup with fixed randomness for consistency.

import os
import sys
import random

WIDTH = 100
HEIGHT = 100
OBSTACLE_DENSITY = 0.08  # ~8% of the map will be walls

# Starting player position
player_x = WIDTH // 2
player_y = HEIGHT // 2

# 2D array to store map tiles: '.' = floor, '#' = wall
game_map = []

def generate_map():
    """
    Generates a 2D map filled with floor tiles and random obstacle tiles.
    The map is created once at startup and stored globally.
    """
    global game_map
    random.seed(42)  # Fixed seed for repeatability during testing
    game_map = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if random.random() < OBSTACLE_DENSITY:
                row.append('#')
            else:
                row.append('.')
        game_map.append(row)

def clear_screen():
    """Clears the terminal screen using the appropriate command for the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    """Reads a single key press without requiring Enter. Cross-platform."""
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
    Draws the entire 100x100 map.
    The player's character '@' is drawn on top of the map tile at their location.
    """
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += '@'
            else:
                row += game_map[y][x]
        print(row)

def update_position(move):
    """
    Updates the player’s position if the destination is not a wall and within bounds.
    """
    global player_x, player_y
    new_x, new_y = player_x, player_y

    if move == 'w':
        new_y -= 1
    elif move == 's':
        new_y += 1
    elif move == 'a':
        new_x -= 1
    elif move == 'd':
        new_x += 1

    # Ensure the new position is inside the map and not an obstacle
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        if game_map[new_y][new_x] != '#':
            player_x, player_y = new_x, new_y

def game_loop():
    """
    Main loop: clears the screen, draws the map, handles input and movement.
    Continues until the user presses 'q'.
    """
    while True:
        clear_screen()
        draw_map()
        print("Use WASD to move. Avoid # walls. Press 'q' to quit.")
        move = get_key()
        if move == 'q':
            break
        update_position(move)

if __name__ == "__main__":
    generate_map()
    game_loop()
