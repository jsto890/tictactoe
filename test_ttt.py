import pytest
from functions_ttt import *


def test_current_turn_number_tricky_board():
    board = ['X', 'O', '.', '.', '.', 'X', '.', '.', 'O']
    count = get_current_turn_number(board)
    assert(count == 5)


def test_current_player_tricky_board():
    board = ['X', 'O', '.', '.', '.', 'X', '.', '.', 'O']
    player = get_current_player(board)
    assert(player == 'Player X')


def test_play_turn_tricky_board():
    a = 1
    b = 3
    board = ['X', 'O', '.', '.', '.', 'X', '.', '.', 'O']
    play_turn(board, a, b)
    assert(board == ['X', 'O', 'X', '.', '.', 'X', '.', '.', 'O'])


def test_check_draw_tricky_board():
    board = ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X', 'O']
    check_draw(board)
    assert exit


def test_check_game_win_tricky_board():
    board = ['O', 'O', 'X', 'O', 'X', 'X', 'X', '.', '.']
    is_win, player = check_win(board)
    assert (player == 'X')