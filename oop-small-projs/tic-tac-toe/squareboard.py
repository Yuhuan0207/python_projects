from board import Board


class Position:
    """(x,y) coordinates on a square board."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) == Position:
            return self.x == other.x and self.y == other.y
        else:
            return super().__eq__(other)

    @staticmethod
    def parse(s):
        """
            Return the position object corresponding to the string.
            s should be of the form 'int, int'.
        """
        comma = s.find(",")
        if comma == -1:
            raise ValueError("No comma in position. Not a valid 2D coordinate.")
        x_pos = int(s[:comma])
        y_pos = int(s[comma + 1:])
        return Position(x_pos, y_pos)

    def __str__(self):
        return f"({self.x}, {self.y})"


class SquareBoard(Board):
    """
        N x N positions arranged in a square board.
    """

    def __init__(self, n):
        super().__init__(n * n)
        self.__size = n

    def __conver_position(self, pos):
        pass

    def __conver_to_position(self, pos):
        pass

    def valid_position(self, pos):
        """Check if input position is a valid position on current board"""
        if isinstance(pos, Position):
            return 0 <= pos.x < self.__size and 0 <= pos.y < self.__size
        else:
            return super().valid_position(pos)

    def all_positions(self):
        pass

    def empty_positions(self):
        pass

    def adjacent_positions(self, pos):
        pass

    def has_object(self, pos):
        pass

    def get_object(self, pos):
        pass

    def remove_object(self, pos):
        pass

    def place_object(self, pos):
        pass

    def __str__(self):
        pass





