# Prompt 0005: Add Screen Clearing and Real-Time Input to Game Loop
# Update the basic ASCII game loop so that the screen clears on every frame and player movement works without pressing Enter.
# Use only built-in libraries. It should work on macOS and Linux in the terminal (no GUI).
# If necessary, use `msvcrt` only on Windows, and fallback to `termios` and `tty` elsewhere.

import os
import sys

WIDTH = 10
HEIGHT = 5

player_x = 4
player_y = 2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    try:
        # Windows
        import msvcrt
        return msvcrt.getch().decode('utf-8').lower()
    except ImportError:
        # POSIX (macOS, Linux)
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
            row += '@' if x == player_x and y == player_y else '.'
        print(row)

def update_position(move):
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
