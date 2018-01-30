from random import randint

# C:\hydra\battleship_one.py

board = []
s = " "
used_coordinates = []

for x in range(0, 8):
    board.append(["-"] * 8)


def print_board(board_in):
    for row in board_in:
        lat = s.join(row)
        print(lat)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def check_for_dups(all_used, row, col):
    """Returning True means these coordinates have NOT been used"""
    bool_var = True
    current = [row, col]
    for ships in all_used:
        # print("The ship coordinate is %s and the list is %s" % (current, ships))
        if current == ships:
            bool_var = False
            # print("False")
            break
    return bool_var


"""Destroyer - 2 spots
Submarine - 3 spots
Cruiser - 3 spots """

destroyer_1_row = random_row(board)
destroyer_1_col = random_col(board)

if randint(0, 1) == 0:
    destroyer_2_row = destroyer_1_row
    if destroyer_1_col == 7:
        destroyer_2_col = destroyer_1_col - 1
    else:
        destroyer_2_col = destroyer_1_col + 1
else:
    destroyer_2_col = destroyer_1_col
    if destroyer_1_row == 7:
        destroyer_2_row = destroyer_1_row - 1
    else:
        destroyer_2_row = destroyer_1_row + 1

used_coordinates.append([destroyer_1_row, destroyer_1_col])
used_coordinates.append([destroyer_2_row, destroyer_2_col])

# print("Destroyer is at %s, %s and %s, %s" % (destroyer_1_row, destroyer_1_col, destroyer_2_row, destroyer_2_col))


all_clear = False
while all_clear is False:
    cruiser_1_row = random_row(board)
    cruiser_1_col = random_col(board)

    if randint(0, 1) == 0:
        cruiser_2_row = cruiser_1_row
        cruiser_3_row = cruiser_1_row
        if cruiser_1_col >= 6:
            cruiser_2_col = cruiser_1_col - 1
            cruiser_3_col = cruiser_1_col - 2
        else:
            cruiser_2_col = cruiser_1_col + 1
            cruiser_3_col = cruiser_1_col + 2
    else:
        cruiser_2_col = cruiser_1_col
        cruiser_3_col = cruiser_1_col
        if cruiser_1_row >= 6:
            cruiser_2_row = cruiser_1_row - 1
            cruiser_3_row = cruiser_1_row - 2
        else:
            cruiser_2_row = cruiser_1_row + 1
            cruiser_3_row = cruiser_1_row + 2

    """Returning True means these coordinates have NOT been used"""
    if check_for_dups(used_coordinates, cruiser_1_row, cruiser_1_col) is False:
        all_clear = False
    elif check_for_dups(used_coordinates, cruiser_2_row, cruiser_2_col) is False:
        all_clear = False
    elif check_for_dups(used_coordinates, cruiser_3_row, cruiser_3_col) is False:
        all_clear = False
    else:
        all_clear = True

used_coordinates.append([cruiser_1_row, cruiser_1_col])
used_coordinates.append([cruiser_2_row, cruiser_2_col])
used_coordinates.append([cruiser_3_row, cruiser_3_col])

# print("Cruiser is at %s, %s : %s, %s : %s, %s" % (cruiser_1_row, cruiser_1_col, cruiser_2_row, cruiser_2_col, cruiser_3_row, cruiser_3_col))

all_clear = False
while all_clear is False:
    submarine_1_row = random_row(board)
    submarine_1_col = random_col(board)

    if randint(0, 1) == 0:
        submarine_2_row = submarine_1_row
        submarine_3_row = submarine_1_row
        if submarine_1_col >= 6:
            submarine_2_col = submarine_1_col - 1
            submarine_3_col = submarine_1_col - 2
        else:
            submarine_2_col = submarine_1_col + 1
            submarine_3_col = submarine_1_col + 2
    else:
        submarine_2_col = submarine_1_col
        submarine_3_col = submarine_1_col
        if submarine_1_row >= 6:
            submarine_2_row = submarine_1_row - 1
            submarine_3_row = submarine_1_row - 2
        else:
            submarine_2_row = submarine_1_row + 1
            submarine_3_row = submarine_1_row + 2

    """Returning True means these coordinates have NOT been used"""
    if check_for_dups(used_coordinates, submarine_1_row, submarine_1_col) is False:
        all_clear = False
    elif check_for_dups(used_coordinates, submarine_2_row, submarine_2_col) is False:
        all_clear = False
    elif check_for_dups(used_coordinates, submarine_3_row, submarine_3_col) is False:
        all_clear = False
    else:
        all_clear = True

used_coordinates.append([submarine_1_row, submarine_1_col])
used_coordinates.append([submarine_2_row, submarine_2_col])
used_coordinates.append([submarine_3_row, submarine_3_col])

# print("Submarine is at %s, %s : %s, %s : %s, %s" % (submarine_1_row, submarine_1_col, submarine_2_row, submarine_2_col, submarine_3_row, submarine_3_col))

# for x in used_coordinates:
    # print(x)

# Everything from here on should be in your for loop
# don't forget to properly indent!
game_over = False
destroyer_sunk = False
cruiser_sunk = False
submarine_sunk = False
turn = 0

print("Welcome to BATTLESHIP!")
print_board(board)
print("There are 3 ships that you must sink.")
print("A destroyer, which is 2 coordinates in size.")
print("A submarine, which is 3 coordinates in size.")
print("A cruiser, which is 3 coordinates in size.")
print("--Be careful though - you can only miss 15 times--")
print(" ")
print("Enter a number between 1 and 8.")

miss_used = 0
while game_over is False:
    # print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    guess_row -= 1
    guess_col -= 1

    if guess_row not in range(8) or guess_col not in range(8):        # checking to see if the guess is out of range
        print("Oops, that's not even in the ocean.")
        miss_used += 1
    elif board[guess_row][guess_col] != "-":                          # Check to see if this guess already happened
        print("You guessed that one already.")
    else:
        if guess_row == destroyer_1_row and guess_col == destroyer_1_col:       # Seeing if the destroyer was hit
            print("*~*~* HIT! *~*~*")
            if board[destroyer_2_row][destroyer_2_col] == "X":
                print("You sank my destroyer!")
                board[destroyer_1_row][destroyer_1_col] = "#"
                board[destroyer_2_row][destroyer_2_col] = "#"
                destroyer_sunk = True
            else:
                board[destroyer_1_row][destroyer_1_col] = "X"
        elif guess_row == destroyer_2_row and guess_col == destroyer_2_col:
            print("*~*~* HIT! *~*~*")
            if board[destroyer_1_row][destroyer_1_col] == "X":
                print("You sank my destroyer!")
                board[destroyer_1_row][destroyer_1_col] = "#"
                board[destroyer_2_row][destroyer_2_col] = "#"
                destroyer_sunk = True
            else:
                board[destroyer_2_row][destroyer_2_col] = "X"
        elif guess_row == cruiser_1_row and guess_col == cruiser_1_col:         # Seeing if the cruiser was hit
            print("*~*~* HIT! *~*~*")
            if board[cruiser_2_row][cruiser_2_col] == "X" and board[cruiser_3_row][cruiser_3_col] == "X":
                print("You sank my cruiser!")
                board[cruiser_1_row][cruiser_1_col] = "#"
                board[cruiser_2_row][cruiser_2_col] = "#"
                board[cruiser_3_row][cruiser_3_col] = "#"
                cruiser_sunk = True
            else:
                board[cruiser_1_row][cruiser_1_col] = "X"
        elif guess_row == cruiser_2_row and guess_col == cruiser_2_col:
            print("*~*~* HIT! *~*~*")
            if board[cruiser_1_row][cruiser_1_col] == "X" and board[cruiser_3_row][cruiser_3_col] == "X":
                print("You sank my cruiser!")
                board[cruiser_1_row][cruiser_1_col] = "#"
                board[cruiser_2_row][cruiser_2_col] = "#"
                board[cruiser_3_row][cruiser_3_col] = "#"
                cruiser_sunk = True
            else:
                board[cruiser_2_row][cruiser_2_col] = "X"
        elif guess_row == cruiser_3_row and guess_col == cruiser_3_col:
            print("*~*~* HIT! *~*~*")
            if board[cruiser_2_row][cruiser_2_col] == "X" and board[cruiser_1_row][cruiser_1_col] == "X":
                print("You sank my cruiser!")
                board[cruiser_1_row][cruiser_1_col] = "#"
                board[cruiser_2_row][cruiser_2_col] = "#"
                board[cruiser_3_row][cruiser_3_col] = "#"
                cruiser_sunk = True
            else:
                board[cruiser_3_row][cruiser_3_col] = "X"
        elif guess_row == submarine_1_row and guess_col == submarine_1_col:         # Seeing if the submarine was hit
            print("*~*~* HIT! *~*~*")
            if board[submarine_2_row][submarine_2_col] == "X" and board[submarine_3_row][submarine_3_col] == "X":
                print("You sank my submarine!")
                board[submarine_1_row][submarine_1_col] = "#"
                board[submarine_2_row][submarine_2_col] = "#"
                board[submarine_3_row][submarine_3_col] = "#"
                submarine_sunk = True
            else:
                board[submarine_1_row][submarine_1_col] = "X"
        elif guess_row == submarine_2_row and guess_col == submarine_2_col:
            print("*~*~* HIT! *~*~*")
            if board[submarine_1_row][submarine_1_col] == "X" and board[submarine_3_row][submarine_3_col] == "X":
                print("You sank my submarine!")
                board[submarine_1_row][submarine_1_col] = "#"
                board[submarine_2_row][submarine_2_col] = "#"
                board[submarine_3_row][submarine_3_col] = "#"
                submarine_sunk = True
            else:
                board[submarine_2_row][submarine_2_col] = "X"
        elif guess_row == submarine_3_row and guess_col == submarine_3_col:
            print("*~*~* HIT! *~*~*")
            if board[submarine_2_row][submarine_2_col] == "X" and board[submarine_1_row][submarine_1_col] == "X":
                print("You sank my submarine!")
                board[submarine_1_row][submarine_1_col] = "#"
                board[submarine_2_row][submarine_2_col] = "#"
                board[submarine_3_row][submarine_3_col] = "#"
                submarine_sunk = True
            else:
                board[submarine_3_row][submarine_3_col] = "X"
        else:                                                                   # If no ships were hit - then it is a miss
            print("~~~ Miss! ~~~")
            board[guess_row][guess_col] = "O"
            miss_used += 1
    if destroyer_sunk is True and cruiser_sunk is True and submarine_sunk is True:
        print("You sunk all my ships!")
        print("Game Over! You win!")
        print_board(board)
        game_over = True
    else:
        print_board(board)
    if miss_used is 15:
        print("You have missed 15 times. You lose!")
        print("You'll just have to try again.")
        break
