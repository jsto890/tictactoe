def initialise_board():
    """
        Initializes the game board with an empty cell in each position.

        Returns:
        board (list): A list of 9 strings, each representing an empty cell on the board.
    """
    board = ('.', '.', '.', '.', '.', '.', '.', '.', '.')
    # Creates the list that forms the board
    board = list(board)
    return board


def display_board(board):
    """
        Displays the current state of the board on the console.

        Args:
        board (list): A list of 9 strings, each representing a cell on the board.
    """
    print(board[0] + '|' + board[1] + '|' + board[2])
    # First line of board
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    # Second line of board
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])
    # Third line of board


def get_current_turn_number(board):
    # Counts the number of turns
    """
        Calculates the current turn number based on the number of moves made on the board.

        Args:
        board (list): A list of 9 strings, each representing a cell on the board.

        Returns:
        turn_number (int): An integer representing the current turn number.
    """
    count = 1
    i = 0
    while i < 9:
        # Repeats through 0 to 8, all our empty cells
        if board[i] != '.':
            # Finds cells that are full and counts them
            count += 1
        i += 1

    return count


def get_current_player(board):
    # Finds the current player that has action on him
    """
        Determines which player's turn it is based on the current state of the board.

        Args:
        board (list): A list of 9 strings, each representing a cell on the board.

        Returns:
        player (str): A string representing the current player, either 'X' or 'O'.
    """
    countX = 0
    countO = 0
    i = 0
    while i < 9:
        if board[i] == 'X':
            # Counts the X plays in progress
            countX += 1
        if board[i] == 'O':
            # Counts the O plays in progress
            countO += 1
        i += 1
    if countX > countO:
        # Compares them and if more X plays then it is player O's turn
        player = 'Player O'

    else:
        # Other option
        player = 'Player X'
    return player


def play_turn(board, a, b):
    """
        Takes the current board state, and the row and column values of the desired move from the
        current player as inputs. It updates the board according to
        the player's move and returns the updated board.

        Args:
        board (list): the current state of the board
        a (int): the row number for the desired move, between 1 and 3
        b (int): the column number for the desired move, between 1 and 3

        Returns:
        board (list): the updated board state after the player's move
    """
    if 1 <= (a and b) <= 3:
        # Values within the range permitted
        c = (3 * (a - 1)) + (b - 1)
        # Correlating coordinates to board number

        count = get_current_turn_number(board)
        # Finding out turns easy within the function
        if count % 2 == 1:
            # Odd = X
            if board[c] == '.':
                # If board is 'empty' player can place their piece
                board[c] = 'X'

            else:
                board[c] = 'O' or 'X'
                # If not then error is printed
                print('This move is not available')

        elif count % 2 == 0:
            # Even  = O
            if board[c] == '.':
                # If board is 'empty' player can place their piece
                board[c] = 'O'

            else:
                board[c] = 'X' or 'O'
                # If not then error is printed
                print('This move is not available')

    else:
        print('This space is not available')


def check_draw(board):
    """
        Function checks the board for a draw

        Args:
        board(list): Current state of the board at the time

        Returns:
        False: If the board is not a draw
    """
    count = get_current_turn_number(board)
    # Brings in count to function
    if count == 10:
        display_board(board)
        print('\nGAME OVER\n')
        # If count reaches 8 then game has tied
        print('PLAYERS HAVE TIED')
        return True
    else:
        return False


def check_win(board):
    """
    Function checks the board for a line of 3 symbols for a win.
    Finds the current turn number to figure out what players turn it is

    Args:
    board: A list representing the current state of the game board.

    Returns:
    If a win condition is found, it returns a tuple (True, player) where player is a string indicating the player who won the game.
    If no win condition is found, it returns False.
    """

    count = get_current_turn_number(board)
    # Finding out turns easy within the function
    countX = 0
    countO = 0
    i = 0
    while i < 9:
        if board[i] == 'X':
            # Counts the X plays in progress
            countX += 1
        if board[i] == 'O':
            # Counts the O plays in progress
            countO += 1
        i += 1
    if countX > countO:
        # Compares them and if more X plays then it is player O's turn
        player = 'X'

    else:
        # Other option
        player = 'O'

    while count >= 5:
        if board[0] == board[1] == board[2] != '.':
            # Along top
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[4] == board[5] != '.':
            # Along middle
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[6] == board[7] == board[8] != '.':
            # Along bottom
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[0] == board[3] == board[6] != '.':
            # Along 1st column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[1] == board[4] == board[7] != '.':
            # Along 2nd column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[5] == board[8] != '.':
            # Along 3rd column
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[0] == board[4] == board[8] != '.':
            # Along L->R diagonal
            display_board(board)
            print('Game has ended')
            print('Well Played ' + player)
            exit()

        elif board[3] == board[4] == board[6] != '.':
            # Along R->L diagonal
            display_board(board)
            print('Game has ended')
            print('Well Played' + player)
            exit()
        return True, player


def play_game():
    """
        This function sets up a new tic-tac-toe board, displays it,
        and allows players to take turns until the game ends in a
        win, a tie, or a player quitting.

        Args:
        None

        Returns:
        None
        """
    board = initialise_board()
    for i in range(10):
        if i == 9:
            exit()
        display_board(board)
        count = get_current_turn_number(board)
        player = get_current_player(board)
        print("Player " + player + " it's your turn, what row do you want to pick?")
        a = input()
        print("Player " + player + " it's your turn, what column do you want to pick?")
        b = input()
        play_turn(board, int(a), int(b))
        check_draw(board)
        check_win(board)

