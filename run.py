# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time

# Global variable:
# Grid for the bord
grid = [[]]

# Grid size
grid_size = 10

# Alphabet for the bord
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Number of ships to place
num_of_ships = 2

# Ship position
ship_position = [[]]

# Number of ships sunk
num_of_ships_sunk = 0

# Bullet left
bullets_left = 50

# Game over
game_over = False


def create_grid():
    """Will create a grid 10x10 and randomly place down ships of different sizes in diffrent directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_position

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []

        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_position = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows -1)
        random_col = random.randint(0, cols -1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)

    if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
