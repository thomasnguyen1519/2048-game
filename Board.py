
import random

class GameBoard:

    __BOARD_SIZE = 4

    def __init__(self):
        self.__board = []
        self.__score = 0
        for i in range(__BOARD_SIZE):
            self.__board.append([0, 0, 0, 0])
        self.__place()

    def is_game_over(self):
        s = set()
        for row in self.__board:
            s.update(row)
        if 0 in s:
            return False
        # check if all the neighbors of each element are different
        temp = []
        temp.append([0] * __BOARD_SIZE)
        for row in self.__board:
            temp.append([0])
            temp[-1].append(row)
            temp[-1].append(0)
        temp.append([0] * __BOARD_SIZE)
        for i in range(1, __BOARD_SIZE + 1):
            for j in range(1, __BOARD_SIZE + 1):
                neighbors = [temp[i][j + 1], temp[i][j - 1], temp[i - 1][j], temp[i + 1][j]]
                if 4 - neighbors.count(0) == len(set(neighbors)):
                    return False
        return True

    def __place(self):
        num = random.choice([2, 4])
        zeros = []
        for i in range(__BOARD_SIZE):
            for j in range(__BOARD_SIZE):
                if self.__board[i][j] == 0:
                    zeros.append((i, j))
        position = random.choice(zeros)
        board[position[0], position[1]] += num
        self.__score += num

    def move(self, ch):
        temp = [row[:] for row in self.__board]

    def __str__(self):
        return str(self.__board)
