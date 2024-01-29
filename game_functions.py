#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def initialize_game():
    """ Initialize the game board with two '2's in random positions. """
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """ Add a new '2' in a random empty spot on the board. """
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2

def compress(board):
    """ Compress the board: move all numbers to the left, no merge. """
    new_board = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge(board):
    """ Merge the board: combine tiles with the same number. """
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    """ Reverse the board: reverse each row. """
    return [row[::-1] for row in board]

def transpose(board):
    """ Transpose the board: swap rows and columns. """
    return [list(row) for row in zip(*board)]

def move_left(board):
    """ Handle a left move. """
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    """ Handle a right move. """
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    """ Handle an up move. """
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    """ Handle a down move. """
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def get_current_state(board):
    """ Check the current state of the game: win, lose, or continue. """
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return 'WIN'
            if board[i][j] == 0 or (j < 3 and board[i][j] == board[i][j + 1]) or (i < 3 and board[i][j] == board[i + 1][j]):
                return 'CONTINUE'
    return 'LOSE'


# In[ ]:




