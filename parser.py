"""
parses an input file which can look something like this:

-------------------------
| 0 0 0 | 0 8 5 | 4 0 0 |
| 3 0 0 | 0 0 9 | 6 0 0 |
| 9 0 0 | 1 0 0 | 0 0 0 |
| ----- | ----- | ----- | 
| 0 4 3 | 0 0 8 | 1 0 0 |
| 0 6 0 | 0 0 0 | 0 2 0 |
| 0 0 0 | 5 0 0 | 7 4 0 |
| ----- | ----- | ----- | 
| 0 0 0 | 0 0 2 | 0 9 1 |
| 0 0 1 | 9 0 0 | 0 0 4 |
| 0 0 5 | 8 3 0 | 0 0 0 |
-------------------------

"""

def is_digit(char):
    """ simple ascii comparison """

    return ord('0') <= ord(char) <= ord('9')


def parse(filename):
    """
    parses input sudoku board from file.
    looking for digits (where 0 means empty cell) and newlines chars. every other character is ignored.
    """

    board = []
    with open(filename) as f:
        for line in f.readlines():
            row = [int(d) for d in line if is_digit(d)]
            if row:
                board.append(row)
    
    assert len(board) == 9 and all(len(row) == 9 for row in board), 'invalid board: not 9x9 digits'
    return board
