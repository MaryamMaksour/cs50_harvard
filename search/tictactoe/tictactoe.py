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
    cnt_x = cnt_o = 0
    
    for row in board:
        for c in row:
            cnt_x += (c == X)
            cnt_o += (c == O)
    
    if cnt_o < cnt_x:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.append((i, j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    board[action[0]][action[1]] = p
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][1] == board[i][0] and board[i][1] == board[i][2] and board[i][1] != EMPTY:
            return board[i][1]
        
        if board[1][i] == board[0][i] and board[1][i] == board[2][i] and board[1][i] != EMPTY:
            return board[1][i]
    
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != EMPTY:
            return board[1][1]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != EMPTY:
            return board[1][1]
    
        
    return "NONE"


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        for c in row:
            if c == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    
    # min for O
    if p == O:
        ans = (-1,-1)
        for action in actions(board):
            if ans == (-1, -1):
                  ans =  action
            res = utility(result(board, action))
            if res == 1:
                continue
            elif res == 0:
                return action
            else:
                ans = action
    else:
        
        ans = (-1,-1)
        for action in actions(board):
            if ans == (-1, -1):
                  ans = action
            res = utility(result(board, action))
            if res == 1:
                continue
            elif res == 0:
                return action
            else:
                ans = action
                
                
    return ans
        
        
    
