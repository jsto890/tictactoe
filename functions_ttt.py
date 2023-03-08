def initialise_board():
    board = ('.', '.', '.', '.', '.', '.', '.', '.', '.')  # Creates the list that forms the board
    board = list(board)
    return board


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])  # First line of board
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])  # Second line of board
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])  # Third line of board


def get_current_turn_number(board):  # Counts the number of turns
    count = 1
    i = 0
    while i < 9:  # Repeats through 0 to 8, all our empty cells
        if board[i] != '.':  # Finds cells that are full and counts them
            count += 1
        i += 1

    return count


def get_current_player(board):  # Finds the current player that has action on him
    countX = 0
    countO = 0
    i = 0
    while i < 9:
        if board[i] == 'X':  # Counts the X plays in progress
            countX += 1
        if board[i] == 'O':  # Counts the O plays in progress
            countO += 1
        i += 1
    if countX > countO:  # Compares them and if more X plays then it is player O's turn
        player = 'Player O'

    else:  # Other option
        player = 'Player X'
    return player


def play_turn(board, a, b):

    if 1 <= (a and b) <= 3:  # Values within the range permitted
        c = (3 * (a - 1)) + (b - 1)  # Correlating coordinates to board number

        count = get_current_turn_number(board)  # Finding out turns easy within the function
        if count % 2 == 1:  # Odd = X
            if board[c] == '.':  # If board is 'empty' player can place their piece
                board[c] = 'X'

            else:
                board[c] = 'O' or 'X'  # If not then error is printed
                print('This move is not available')

        elif count % 2 == 0:  # Even  = O
            if board[c] == '.':  # If board is 'empty' player can place their piece
                board[c] = 'O'

            else:
                board[c] = 'X' or 'O'  # If not then error is printed
                print('This move is not available')

    else:
        print('This space is not available')


def check_draw(board):
    count = get_current_turn_number(board)  # Brings in count to function
    if count == 10:
        display_board(board)
        print('\nGAME OVER\n')  # If count reaches 8 then game has tied
        print('PLAYERS HAVE TIED')
        exit()
    else:
        return False


def check_win(board):

    count = get_current_turn_number(board)  # Finding out turns easy within the function
    countX = 0
    countO = 0
    i = 0
    while i < 9:
        if board[i] == 'X':  # Counts the X plays in progress
            countX += 1
        if board[i] == 'O':  # Counts the O plays in progress
            countO += 1
        i += 1
    if countX > countO:  # Compares them and if more X plays then it is player O's turn
        player = 'Player X'

    else:  # Other option
        player = 'Player O'

    while count >= 5:
        if board[0] == board[1] == board[2] != '.':  # Along top
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[4] == board[5] != '.':  # Along middle
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[6] == board[7] == board[8] != '.':  # Along bottom
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[0] == board[3] == board[6] != '.':  # Along 1st column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[1] == board[4] == board[7] != '.':  # Along 2nd column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[5] == board[8] != '.':  # Along 3rd column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[0] == board[4] == board[8] != '.':  # Along L->R diagonal
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[4] == board[6] != '.':  # Along R->L diagonal
            display_board(board)
            print('Game has ended')
            print('Well Played' + player)
            exit()
        return True, player


def play_game():
    board = initialise_board()
    for i in range(10):
        display_board(board)
        count = get_current_turn_number(board)
        player = get_current_player(board)
        print(player + " it's your turn, what row do you want to pick?")
        a = input()
        print(player + " it's your turn, what column do you want to pick?")
        b = input()
        play_turn(board, int(a), int(b))
        check_draw(board)
        check_win(board)

