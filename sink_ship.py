# Sink ship game based on codecademy.com python exercise
# For python 3

# Färg för lättare läsbarhet av spelbrädet
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


from random import randint

board = []

# bygger spelbrädet mha listor
for x in range(5):
    board.append(["O"] * 5)


def print_board(board):

    # snyggar upp matrisen: tar bort kommaseparering och sånt
    for row in board:
        print(" ".join(row))


def rand_ship_gen():
    preliminary_row = randint(0, len(board) - 1)
    preliminary_col = randint(0, len(board[0]) - 1)

    ship_coord = [preliminary_row, preliminary_col]

    return ship_coord


print("\nLet's play Battleship!")
print_board(board)

# OBS!! Med ett 5x5 bräde kan det max vara 25 skepp.
# Är siffran > 25 fastnar while-loopen för då finns
# alla möjliga värden redan i listan!
number_of_ships = int(input("Hur många skepp? "))

the_ships = []

# Första motståndarskeppet läggs till.
# Det finns ju alltid minst ett så därför sker detta separat.
the_ships.append(rand_ship_gen())
count = 1
green_light = True

# Ev. resterande skepp tas fram, dubblett-kontrolleras och läggs till.
while count < number_of_ships:

    rand_ship = rand_ship_gen()

    if rand_ship in the_ships:
        green_light = False

    else:
        green_light = True

    if green_light == True:
        the_ships.append(rand_ship)
        count += 1
    else:
        pass

hit_marker = bcolors.BOLD + bcolors.OKGREEN + "X" + bcolors.ENDC
miss_marker = bcolors.BOLD + bcolors.FAIL + "X" + bcolors.ENDC


# man får fyra försök på sig
print(the_ships)

turns = 4

for turn in range(turns):
    
    print("\nTurn", turn + 1, "of", turns)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    guess_coord = [guess_row, guess_col]
    
    # utanför koordinatsystemet?
    if not (0 <= guess_row <= 4) or not (0 <= guess_col <= 4):
        print("Oops, that's not even in the ocean.")

    # gissa samma som tidigare?
    # == "X" funkar inte pga färgerna?
    # == hit_marker or miss_marker borde då funka
    elif board[guess_row][guess_col] != "O":
            print("You guessed that one already.")
    
    elif guess_coord in the_ships:
        print("Congratulations! You sunk a battleship!")
        
        board[guess_row][guess_col] = hit_marker
        
        number_of_ships -= 1
        
        if number_of_ships > 0:
            print(number_of_ships, "to go!")
        else:
            print("\nYou win!\n")
            print_board(board)
            break

    # Inget annat krav uppnått? dä är det miss!
    else:
        print("You missed!")

        # kryssar för gissad ruta på spelbrädet
        # syntax för bcolors klassen
        board[guess_row][guess_col] = miss_marker
        
    # sista omgången?
    if turn == turns - 1:
        print("\nGame Over\n")
    else:
        pass

    print("")
    print_board(board)
