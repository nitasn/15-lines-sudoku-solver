"""
generates a random sudoku board (in its solved state).
"""

from engine import solutions, candidates
from pretty_print import pretty_print
from random import shuffle


def generate_random_board():
    """ returns a random board in its solved state """

    all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    board = [[0] * 9 for _ in range(9)]

    for sqr in (0, 3, 6):     # randmoly filling the 1st, 5th, 9th 
        shuffle(all_nums)     # 3x3 squares (see picture below)
        for k in range(9):
            board[sqr + (k // 3)][sqr + (k % 3)] = all_nums[k]

    ''' 
    now the board looks like this:

    7 4 1  0 0 0  0 0 0  
    3 2 6  0 0 0  0 0 0  
    5 8 9  0 0 0  0 0 0  

    0 0 0  4 1 3  0 0 0  
    0 0 0  5 7 2  0 0 0  
    0 0 0  8 9 6  0 0 0  

    0 0 0  0 0 0  1 9 4  
    0 0 0  0 0 0  7 5 8  
    0 0 0  0 0 0  2 3 6  '''

    try:
        solutions_iter = solutions(board)
        return next(solutions_iter)

    except StopIteration:
        # if generated unsolvable initial state (didn't happen in my tests but cannot prove it can't happen) then
        return generate_random_board()  # try again with a different initial state...


if __name__ == '__main__':
    print('\ngenerating random board...\n')
    pretty_print(generate_random_board())
