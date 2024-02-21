class Board:

    def __init__(self, columns, rows):
        self.__columns = columns
        self.__rows = rows
        self.__initialize_board()

    def __initialize_board(self):
        self.__board = []
        for i in range(0, self.__rows):
            row = []
            for j in range(0, self.__columns):
                row.append(" ")
            self.__board.append(row)

    def print_board(self):
        self.__print_numbers()
        self.__print_line()
        for row in self.__board:
            self.__print_row(row)

    def __print_line(self):
        line = " "
        line += "_" * (self.__columns * 4 - 1)
        line += " "
        print(line)

    def __print_row(self, row):
        line = "|"
        for i in range(0, self.__columns):
            line += f" {row[i]} |"
        print(line)
        self.__print_line()

    def __print_numbers(self):
        line = " "
        for i in range(0, self.__columns):
            header = i + 1
            if header < 10:
                line += f" {header} "
            else:
                line += f" {header}"
    
    def add_token(self, row, column, token):
        self.__board[row][column] = token

    def check_row(self, column):
        for i in range(self.__rows - 1, -1, -1):
            if self.__board[i][column] == " ":
                return i
        return -1

    def is_valid_column(self, column):
        return 0 <= column < self.__columns



