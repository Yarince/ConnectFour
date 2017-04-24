from Functions import print_board


class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ConnectFour:
    __width = 7
    __height = 6

    __player = 1

    def __init__(self):
        self.__game_board = [[0 for i in range(self.__width)] for j in range(self.__height)]
        # noinspection PyTypeChecker
        self.__game_board.append(['--' * self.__width])
        self.__game_board.append([])
        for i in range(self.__width):
            self.__game_board[self.__height + 1].append(i + 1)

    def run(self):
        str_place = ''
        while True:
            print_board(self.__game_board)
            try:
                str_place = input("Player %d\nWhere do you want to place?\n" % self.__player)
                place = int(str_place) - 1
                if place > self.__width:
                    raise ValueError
            except ValueError:
                if str_place == 'x':
                    break
                print(ConsoleColors.FAIL + "\nThat's not a row number!\n" + ConsoleColors.ENDC)
                continue

            if not self.check_valid_move(place):
                if self.calculate_fall(place) >= 0:
                    self.__game_board[self.calculate_fall(place)][place] = self.__player
                    print_board(self.__game_board)
            else:
                print("row is full try again")
                continue

            if self.is_winner(self.__game_board, self.__player):
                print("Player %d won" % self.__player)
                break
            self.__player = 2 if self.__player == 1 else 1

    def is_winner(self, board, tile):
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

    def check_valid_move(self, column):
        return self.__game_board[0][column] > 0

    def calculate_fall(self, column):
        i = 0
        while i < self.__height:
            if self.__game_board[i][column] > 0:
                return i - 1
            elif i == self.__height - 1 and self.__game_board[self.__height - 1][column] == 0:
                return i
            i += 1
        return -1337


def main():
    ConnectFour().run()


if __name__ == '__main__':
    main()
