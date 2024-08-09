"""
Tic Tac Toe Player
"""

import math, copy

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
    x_count = 0
    o_count = 0
    for i in board:
        x_count += i.count(X)
        o_count += i.count(O)

    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = copy.deepcopy(board)
    if action:
        i, j = action
        board[i][j] = player(board)
        return board
    else:
        raise 'problem';


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    tmp = []
    tmp_r = []
    big = []
    for i in range(3):
        
        # horizontal check
        big.append(board[i].copy())
        t = []
        for j in range(3):

            # diagonal checks
            if i == j:
                tmp.append(board[i][j])
            if i + j == 2:
                tmp_r.append(board[i][j])
            t.append(board[j][i])
        big.append(t)

    big += [tmp] + [tmp_r]
    for i in big:
        if all(j == i[0] and i[0] != EMPTY for j in i):
            return i[0]
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    for i in board:
        if EMPTY in i:
            return False
    return True
            

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board):
        return 1 if player(board) == O else -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if board == initial_state():
        return (0,0) 
    action = None
    
    if player(board) == X:
        tmp = -math.inf
        for i in actions(board):
            a = max_val(board, i)
            if tmp < a:
                action = i
                tmp = a
    else:
        tmp = math.inf
        for i in actions(board):
            a = min_val(board, i)
            if tmp > a:
                action = i
                tmp = a
    return action
    pass

def max_val(board, action):
    t_board = result(board, action)
    if terminal(t_board):
        return utility(t_board)
    else:
        v = math.inf
        for i in actions(t_board):
            v = min(min_val(t_board, i), v)
        return v


def min_val(board, action):
    r_board = result(board, action)
    if terminal(r_board):
        return utility(r_board)
    else:
        v = -math.inf
        for i in actions(r_board):
            v = max(max_val(r_board, i), v)
        return v
