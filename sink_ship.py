# Sink ship game based on codecademy.com python exercise
# For python 3



from random import randint

board = []

# bygger spelbrädet mha listor
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):

    # snyggar upp matrisen: tar bort kommaseparering och sånt
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)


the_ships = []

number_of_ships = 2

# skapa skeppskoordinat-matrisen
for y in range(0, number_of_ships):
    the_ships.append(['A'] * 2)

print(the_ships)

# dolt-skepp-generator
for ship in range(0, number_of_ships):

    #the_ships.append(['0'] * 2)

    while True:
        #print(len(board))
        #print(board[0])
        check_collide_row = randint(0, len(board) - 1) # row

        check_collide_col = randint(0, len(board[0]) - 1) # col
        #print(check_collide_row, check_collide_col)
        for x in range(0, number_of_ships):
            #print(x)
            if check_collide_row == the_ships[x][0] and check_collide_col == the_ships[x][1]:
                pass

            else:
                the_ships[ship][0] = check_collide_row

                the_ships[ship][1] = check_collide_col

                break


#print(the_ships)

#    def random_row(board):
#        return randint(0, len(board) - 1)

#    def random_col(board):
#        return randint(0, len(board[0]) - 1)

#ship_row = random_row(board)
#ship_col = random_col(board)
#debug output nedan
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!

# man får fyra försök på sig
for turn in range(4):

    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1

    # vinnarkravet
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")

        # avbryter loopen så spelet slutar på försöket man vinner
        break

    # miss-trädet
    else:

        # utanför koordinatsystemet
        if not (0 <= guess_row <= 4) or not (0 <= guess_col <= 4):
            print("Oops, that's not even in the ocean.")

        # för när man gissar samma som tidigare
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")

            # kryssar för gissad ruta på spelbrädet
            board[guess_row][guess_col] = "X"

        # om detta var sista omgången så följer game over
        if turn == 3:
            print('Game Over')

        print('That\'s turn %d out of 4' % (turn + 1))

        print_board(board)
