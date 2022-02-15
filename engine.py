def candidates(board, i, j):
    """ returns set of candidate digits that can go into board[i][j] """

    row = {board[i][k] for k in range(9)}
    col = {board[k][j] for k in range(9)}
    sqr = {board[i - (i % 3) + (k // 3)][j - (j % 3) + (k % 3)] for k in range(9)}

    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - row - col - sqr


def solutions(board):
    """ yields all solved states of the board (assuming it was legal when we got it) """

    empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

    if empty_cells:
        i, j = min(empty_cells, key=lambda coords: len(candidates(board, *coords)))  # cell of least options

        for digit in candidates(board, i, j):
            board[i][j] = digit
            yield from solutions(board)
            board[i][j] = 0

    else:
        yield [row[:] for row in board]  # clone solved state (gonna test more solutions on the board)
        
