from Functions import print_board
from board import Board
from console_color import ConsoleColors


class ConnectFour:
    __width = 7
    __height = 6

    __player = 1

    def __init__(self):
        self.__game_board = Board(self.__width, self.__height)

    def run(self):
        while True:
            print_board(self.__game_board.get_board())
            place = self.get_place_from_input()

            if self.__game_board.check_valid_move(place):
                self.__game_board.move(place, self.__player)
                print_board(self.__game_board.get_board())
            else:
                print("Row is full try again")
                continue
            if self.game_won():
                break
            self.switch_player()

    def game_won(self):
        if self.__game_board.is_winner(self.__player):
            print("Player %d won" % self.__player)
            return True
        return False

    def switch_player(self):
        self.__player = 2 if self.__player == 1 else 1

    def get_place_from_input(self):
        place = 0
        try:
            place = int(input("Player %d\nWhere do you want to place?\n" % self.__player)) - 1
            if place > self.__width:
                raise ValueError
        except ValueError:
            print(ConsoleColors.FAIL + "\nThat's not a row number!\n" + ConsoleColors.ENDC)
        return place
