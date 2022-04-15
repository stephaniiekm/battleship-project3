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
        random_row = random.randint(0, rows-1)
        random_col = random.randint(0, cols-1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)

    if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
        num_of_ships_placed += 1


def print_grid():

    global print_grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=" ")

    for col in range(len(grid[row])):
        if grid[row][col] == "0":
            if debug_mode:
                print("0", end=" ")
            else:
                print(".", end=" ")
        else:
            print(grid[row][col], end=" ")

    print("")
    
    print(" ", end=" ")

    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")


def try_to_place_ship_on_grid(row, col, direction, length):

    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length
    
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
    
    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length
    
    return validate_grid_and_place_ship(start_col, end_col, start_row, end_row)


def accept_valid_bullet_placement():

    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-J) and column (8-9) such as A3: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column such as A3")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter letter (A-J) for row and (8-9) column")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter letter (A-J) for row and (8-9) column")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter letter (A-J) for row and (8-9) column")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You have alredy shot a bullet here, choose another spot")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            is_valid_placement = True
    
    return row, col

def check_for_ship_sunk(row, col):

    global ship_position
    global grid

    for position in ship_position:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True

def shoot_bullet():

    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".":
        print("You missed, no ship was shot")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("A ship was completely sunk!")
            num_of_ships_sunk += 1
        else:
            print("A ship was shot")
    
    bullets_left -= 1


def check_for_game_over():

    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congratulations you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! No bullets left, better luck next time!")
        game_over = True



