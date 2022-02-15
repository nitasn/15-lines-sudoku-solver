_ = 0

board = [
    [_,_,_,  _,_,9,  6,4,_],
    [_,_,2,  7,_,_,  5,_,3],
    [_,9,_,  _,_,4,  2,1,8],

    [_,6,1,  8,7,_,  _,_,_],
    [_,8,_,  _,_,_,  _,2,_],
    [_,_,_,  _,4,6,  8,5,_],

    [1,4,5,  6,_,_,  _,8,_],
    [9,_,6,  _,_,1,  3,_,_],
    [_,3,8,  4,_,_,  _,_,_]
]


from prettier_print import prettier_print
from engine import solutions

for solution in solutions(board):
    prettier_print(solution)
