# Prompt 0003: Add Basic ASCII Game Loop with WASD Movement
# Create the simplest possible game loop in Python that runs in the terminal and redraws a small ASCII map on every iteration.
# The player should be represented by '@' and should be able to move up, down, left, and right using the WASD keys.
# Use only built-in libraries. Do not worry about real-time input or screen clearing yet — just focus on the loop and basic movement logic.

WIDTH = 10
HEIGHT = 5

# Starting player position
player_x = 4
player_y = 2

def draw_map():
    for y in range(HEIGHT):
        row = ''
        for x in range(WIDTH):
            if x == player_x and y == player_y:
                row += '@'
            else:
                row += '.'
        print(row)

def handle_input():
    move = input("Move (WASD): ").lower()
    return move if move in ['w', 'a', 's', 'd'] else None

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
        draw_map()
        move = handle_input()
        if move:
            update_position(move)
        print("\n" * 2)  # Add spacing between frames

if __name__ == "__main__":
    game_loop()
