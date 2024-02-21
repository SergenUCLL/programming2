from player import Player
from board import Board

class Game:

    def __init__(self):
        print("welcome to connect4")

        p1 = Player("Bart", "X")
        p2 = Player("Dries", "O")

        print(p1.name)
        print(p2.name)
        
        board = Board(7,6)
        board.print_board()

        won = False
        while not won:

            selection = input(f"{p1.name}, please input your selection")

            if not selection.isnumeric():
                print("wrong choice no number, try again")
                continue #stopt met de rest van de lus en begint gwn met de volgende while ipv telkens met if else

            column = int(selection) - 1
            if not board.is_valid_column(column):
                print("wrong choice")
                continue

            #input = 1
            row = board.check_row(column)

            if row == -1:
                print("wrong")
                continue
            
            board.add_token(row, column, p1.token)
            board.print_board()

game = Game()