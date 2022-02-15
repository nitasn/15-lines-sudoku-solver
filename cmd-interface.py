from prettier_print import prettier_print as pretty_print
from engine import solutions
from parser import parse
from sys import argv


def main():
    """ get the board, pass it to 'solutions', then print them results """

    board = handle_args()
    solved_states = [*solutions(board)]

    print(f'\nfound {len(solved_states)} solution(s)...\n')

    for solution in solved_states:
        print()
        pretty_print(solution)


def handle_args():
    """ greets, explains correct use, blah blah. if success, returns board read from file given by args """

    if len(argv) == 1:
        print('\nwelcome to sudoku solvoer!\n')
        print('input file should hold a sudoku board of 9x9 digits,')
        print('where 0 means empty and newline separates between rows (every other char is ignored).')
    
    if len(argv) != 2:
        print(f'\nusage: python3 {argv[0]} input_file\n')
        exit()
    
    try:
        board = parse(filename=argv[1])
    except AssertionError as e:
        print('\nerror parsing file. err msg:', e, '\n')
        exit()
    except FileNotFoundError as e:
        print('\nfile not found. err msg:', e, '\n')
        exit()
    
    return board


if __name__ == "__main__":
    main()
