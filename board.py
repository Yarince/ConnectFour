class Board:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__game_board = [[0 for i in range(self.__width)] for j in range(self.__height)]
        # noinspection PyTypeChecker
        self.__game_board.append(['--' * self.__width])
        self.__game_board.append([])
        for i in range(self.__width):
            self.__game_board[self.__height + 1].append(i + 1)

    def check_valid_move(self, column):
        return self.__game_board[0][column] == 0

    def get_board(self):
        return self.__game_board

    def is_winner(self, tile):
        board = self.__game_board
        # check horizontal spaces
        for x in range(self.__height - 3):
            for y in range(self.__width):
                if board[x][y] == tile \
                        and board[x + 1][y] == tile \
                        and board[x + 2][y] == tile \
                        and board[x + 3][y] == tile:
                    return True
        # check vertical spaces
        for x in range(self.__height):
            for y in range(self.__width - 3):
                if board[x][y] == tile \
                        and board[x][y + 1] == tile \
                        and board[x][y + 2] == tile \
                        and board[x][y + 3] == tile:
                    return True
        # check / diagonal spaces
        for x in range(self.__height - 3):
            for y in range(3, self.__width):
                if board[x][y] == tile \
                        and board[x + 1][y - 1] == tile \
                        and board[x + 2][y - 2] == tile \
                        and board[x + 3][y - 3] == tile:
                    return True
        # check \ diagonal spaces
        for x in range(self.__height - 3):
            for y in range(self.__width - 3):
                if board[x][y] == tile \
                        and board[x + 1][y + 1] == tile \
                        and board[x + 2][y + 2] == tile \
                        and board[x + 3][y + 3] == tile:
                    return True
        return False

    def calculate_fall(self, column):
        i = 0
        while i < self.__height:
            if self.__game_board[i][column] > 0:
                return i - 1
            elif i == self.__height - 1 and self.__game_board[self.__height - 1][column] == 0:
                return i
            i += 1
        return -1337

    def move(self, place, player):
        if self.check_valid_move(place):
            if self.calculate_fall(place) >= 0:
                self.__game_board[self.calculate_fall(place)][place] = player
            return True
        else:
            return False
