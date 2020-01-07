
import random

class GameBoard:

    BOARD_SIZE = 4

    def __init__(self):
        self.__board = []
        self.__score = 0
        for i in range(GameBoard.BOARD_SIZE):
            self.__board.append([0, 0, 0, 0])
        self.__place_block()

    def score(self):
        return self.__score

    def is_game_over(self):
        if self.has_zeros():
            return False
        # check if all the neighbors are different to the element
        temp = []
        temp.append([0] * (GameBoard.BOARD_SIZE + 2))
        for row in self.__board:
            temp.append([0])
            temp[-1].extend(row)
            temp[-1].append(0)
        temp.append([0] * (GameBoard.BOARD_SIZE + 2))
        for i in range(1, GameBoard.BOARD_SIZE + 1):
            for j in range(1, GameBoard.BOARD_SIZE + 1):
                neighbors = [temp[i][j + 1], temp[i][j - 1], temp[i - 1][j], temp[i + 1][j]]
                uniq = set(neighbors)
                if temp[i][j] in uniq:
                    return False
        return True

    def has_zeros(self):
        s = set()
        for row in self.__board:
            s.update(row)
        return 0 in s

    def __place_block(self):
        if self.has_zeros():
            num = random.choice([2, 4])
            zeros = []
            for i in range(GameBoard.BOARD_SIZE):
                for j in range(GameBoard.BOARD_SIZE):
                    if self.__board[i][j] == 0:
                        zeros.append((i, j))
            position = random.choice(zeros)
            self.__board[position[0]][position[1]] += num
            self.__score += num

# TODO: (bug) move doesnt change board state -> shouldnt place a new block
    def move(self, ch):
        if ch == 'w':
            self.cascade_up()
        elif ch == 's':
            self.cascade_down()
        elif ch == 'a':
            self.cascade_left()
        elif ch == 'd':
            self.cascade_right()
        if self.has_zeros():
            self.__place_block()

    def cascade_left(self):
        # bubble zeros to the right, add left, append extra zeros
        for row in self.__board:
            i = GameBoard.BOARD_SIZE - 1
            while i >= 0:
                if row[i] == 0:
                    row.append(row.pop(i))
                i -= 1
        for row in self.__board:
            for i in range(GameBoard.BOARD_SIZE - 1):
                if row[i + 1] == 0:
                    break
                if row[i] == row[i + 1]:
                    row[i] += row[i + 1]
                    self.__score += row[i]
                    row.pop(i + 1)
                    row.append(0)

    def cascade_right(self):
        # bubble zeros to the left, add right, insert extra zeros
        for row in self.__board:
            i = 0
            while i < GameBoard.BOARD_SIZE:
                if row[i] == 0:
                    row.insert(row.pop(i), 0)
                i += 1
        for row in self.__board:
            for i in range(GameBoard.BOARD_SIZE - 1, 0, -1):
                if row[i - 1] == 0:
                    break
                if row[i] == row[i - 1]:
                    row[i] += row[i - 1]
                    self.__score += row[i]
                    row.pop(i - 1)
                    row.insert(0, 0)

    def cascade_up(self):
        self.__board = self.__transpose()
        self.cascade_left()
        self.__board = self.__transpose()

    def cascade_down(self):
        self.__board = self.__transpose()
        self.cascade_right()
        self.__board = self.__transpose()

    def __transpose(self):
        return [[self.__board[i][j] for i in range(len(self.__board))] for j in range(len(self.__board))]

    def __str__(self):
        return "\n".join([str(row) for row in self.__board])
