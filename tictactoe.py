"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board [row][col] == X:
                countX += 1
            elif board [row][col] == 0:
                countO += 1
    return X if countX == countO else 0


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                # add the tuple to the possible_moves set as a tuple
                possible_moves.add((row, col)) 
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action

    if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
        raise IndexError()

    newBoard = [row[:] for row in board]
    newBoard[x][y] = player(board)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRows(board, X)  or checkColumns(board, X) or checkTopBottomDiagonal(board, X) or checkBottomTopDiagonal(board, X):
        return X
    elif checkRows(board, O)  or checkColumns(board, O) or checkTopBottomDiagonal(board, O) or checkBottomTopDiagonal(board, O):
        return O
    else:
        return None

def checkRows(board, player):
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player: 
                count += 1
        if count == len(board[0]):
            return True
    return False


def checkColumns(board, player):
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][col] == player: 
                count += 1
        if count == len(board[0]):
            return True
    return False

def checkTopBottomDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range (len(board[0])):
            if row==col and board[row][col] == player:
                count += 1
    return count == len(board[0])

def checkBottomTopDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range (len(board[0])):
            if (len(board)-row-1) == col and board[row][col] == player:
                count += 1
    return count == len(board[0])

def tie(board, palyer):
    countEmpty = (len(board)) * (len(board[0]))
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                countEmpty -= 1
    return == 0


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner (board) or tie(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
