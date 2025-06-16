# Prompt 0006: Expand Game Board and Add Explanatory Comments
# Triple the size of the game board and add high-quality comments that explain the purpose and design of each function and key section.

import os
import sys

# Game world dimensions (increased from 10x5 to 30x15)
WIDTH = 30
HEIGHT = 15

# Initial player position at the center of the expanded map
player_x = WIDTH // 2
player_y = HEIGHT // 2

def clear_screen():
    """
    Clears the terminal screen.
    Uses 'cls' for Windows and 'clear' for POSIX systems.
    Called every frame to redraw the screen from scratch.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    """
    Reads a single key press from the user without requiring Enter.
    Uses msvcrt for Windows and termios/tty for macOS/Linux.
    Returns the lowercase character pressed.
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
    Draws the entire game world.
    Prints a grid of WIDTH x HEIGHT, placing '@' at the player's current position,
    and '.' everywhere else.
    """
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += '@'
            else:
                row += '.'
        print(row)

def update_position(move):
    """
    Updates the player's position based on the input key.
    Enforces world boundaries so the player cannot move off the map.
    """
    global player_x, player_y
    if move == 'w' and player_y > 0:
        player_y -= 1
    elif move == 's' and player_y < HEIGHT - 1:
        player_y += 1
    elif move == 'a' and player_x > 0:
        player_x -= 1
    elif move == 'd' and player_x < WIDTH - 1:
        player_x += 1

def game_loop():
    """
    Main game loop.
    Continuously clears the screen, renders the map,
    waits for user input, and updates the player's position.
    Loops until the user presses 'q'.
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
    game_loop()
