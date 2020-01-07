
import Board

def main():
    intro()
    explain_controls()
    play_game()

def intro():
    print()
    print('This is a program that plays the 2048 game.')
    print('You combine like-numbered blocks on the game board,')
    print('and the objective is to make the illusive 2048 block.')
    print('Try to accumulate the highest score if that is too easy.')
    print('It currently runs in the console, but don\'t worry')
    print('it will be ported over to a GUI soon :).')
    print()
    print('Let\'s start playing!!')
    print()

def explain_controls():
    print('Use the W-A-S-D keys to cascade the blocks in a certain')
    print('direction. W cascades upwards. A cascades left.')
    print('S cascades downwards. D cascades right.')
    print()
    print('Goodluck!')
    print()

def play_game():
    board = Board.GameBoard()
    while not board.is_game_over():
        print('Score:', board.score(), end = '\n\n')
        print(board, end = '\n\n')
        print('What move would you like to make (', 'w, ', 'a, ', 's, ', 'd)? ', sep = "", end = "")
        move = str(input())
        while move != 'w' and move != 'a' and move != 's' and move != 'd':
            print('Invalid move.')
            print()
            print('What move would you like to make (', 'w, ', 'a, ', 's, ', 'd)? ', sep = "", end = "")
            move = str(input())
        print()
        board.move(move)
    print(board, end = '\n\n')
    print('Game over!!', end = '\n\n')
    print('Your score was ' + board.score() + '!')

if __name__ == '__main__':
    main()
