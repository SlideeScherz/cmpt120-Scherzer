# tic tac toe
# x always goes first

'''define the list'''
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


'''shows the user the spot numebring system'''
print(0, '|', 1, '|', 2)
print('-'*9)
print(3, '|', 4, '|', 5)
print('-'*9)
print(6, '|', 7, '|', 8)
print()
print()


# print the board after every move
def printboard():
    print(board[0], '|', board[1], '|', board[2])
    print('-'*9)
    print(board[3], '|', board[4], '|', board[5])
    print('-'*9)
    print(board[6], '|', board[7], '|', board[8])


'''define a function to check list return a win or loss'''
# top 3 is vertical win
# middle 3 is horizonal win
# last 2 is horizontal win


def santa(i):
    if (board[0] == i and board[1] == i and board[2] == i):
        return True
    elif (board[3] == i and board[4] == i and board[5] == i):
        return True
    elif (board[6] == i and board[7] == i and board[8] == i):
        return True

    elif (board[0] == i and board[3] == i and board[6] == i):
        return True
    elif (board[1] == i and board[4] == i and board[7] == i):
        return True
    elif (board[2] == i and board[5] == i and board[8] == i):
        return True

    elif (board[0] == i and board[4] == i and board[8] == i):
        return True
    elif (board[2] == i and board[4] == i and board[6] == i):
        return True

    else:
        return False


# replace a space with an x or o
# check if move is valid
# print board
# check that move is valid
# STORE THE MOVE AS AN INT
# BUT X or O MUST BE STORED AS STR

def movemaker(turn):
    while True:
        print('player', turn, 'its your turn')
        move = int((input("where would you like to move?: ")))

        if (move < 9 and board[move] == ' '):
            board[move] = turn
            break  # ONLY BREAK IF MOVE IS VALID
        else:
            print('not a valid move')  # restart upon error

    printboard()


'''game loop'''
# loop untill there is a winner, or spaces are full
win = False
turn = 0

while True:
    movemaker('x')
    win = santa('x')
    turn = turn + 1

    if win == True:
        print('x wins!')
        break

    if turn == 9:
        print('its a tie')
        break

    movemaker('o')
    win = santa('o')
    turn = turn + 1

    if win == True:
        print('o wins!')
        break

    if turn == 9:
        print('its a tie')
        break
