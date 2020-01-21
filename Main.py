
import Board
import json
import sys

# serialize and deserialize a board

def main():
    intro()
    explain_controls()
    data = load_data('data.json')
    play_game(data)

def intro():
    print('\nThis is a program runs the classic 2048 game.')
    print('You combine like-numbered blocks on the game board,')
    print('and the objective is to make the illusive 2048 block.')
    print('Try to accumulate the highest score if that is too easy.')
    print('It currently runs in the console, but don\'t worry')
    print('it will be ported over to a GUI soon :).', end = '\n\n')
    print('Let\'s start playing!!', end = '\n\n')

def explain_controls():
    print('Use the W-A-S-D keys to cascade the blocks in a certain')
    print('direction. W cascades upwards. A cascades left.')
    print('S cascades downwards. D cascades right.', end = '\n\n')
    print('Goodluck!', end = '\n\n')

def main_menu():
    pass

def load_data(rel_path):
    try:
        data_file = open(rel_path)
    except FileNotFoundError:
        print(rel_path, ' file was not found.')
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("An unexpected error occured when loading the file.")
        print("Shutting down...")
        sys.exit(1)
    else:
        data = json.load(data_file)
        return data["hiscore"], data["largest_block"]

def play_game(hiscores):
    board = Board.GameBoard()
    print('All Time Hiscore:', hiscores[0])
    print('Largest block built:', hiscores[1])
    while not board.is_game_over():
        print('\nScore:', board.score(), end = '\n\n')
        print(board, end = '\n\n')
        print('What move would you like to make? Up (w), Left (a), Down (s), Right (d)? ', sep = "", end = "")
        move = str(input())
        while move != 'w' and move != 'a' and move != 's' and move != 'd':
            print('Invalid move.', end = '\n\n')
            print('What move would you like to make (', 'w, ', 'a, ', 's, ', 'd)? ', sep = "", end = "")
            move = str(input())
        board.move(move)
    print(board, end = '\n\n')
    print('Game over!!', end = '\n\n')
    print('Your score was ' + str(board.score()) + '!', end = "\n\n")
    print('Saving your score...')
    if hiscores[0] <= board.score() or hiscores[1] <= board.largest_block():
        data = {"hiscore": max(hiscores[0], board.score()), "largest_block": max(hiscores[1], board.largest_block())}
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile, skipkeys = True, indent = 4)
    print('Done.\n')


if __name__ == '__main__':
    main()
