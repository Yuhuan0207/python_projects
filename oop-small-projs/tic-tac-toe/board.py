from gamestate import GameState


class Board(GameState):
    """
    Board game state. Each position contains an object(or nothing).
    """

    def __init__(self, size: int) -> None:
        """Initialize the board with size. Each position contains nothing."""
        self._positions = [None for i in range(size)]

    def copy(self):
        pass

    def valid_position(self, position) -> bool:
        return 0 <= position < len(self._positions)

    def all_positions(self) -> [int]:
        return [position for position in range(len(self._positions))]

    def empty_positions(self) -> [int]:
        """Return empty positions in board."""
        return [position for position in range(len(self._positions))
                if not self.has_object(position)]
    
    def has_object(self, position) -> bool:
        assert self.valid_position(position)
        return self._positions[position] is not None
    
    def get_object(self, position):
        assert self.valid_position(position)
        return self._positions[position]

    def remove_object(self, position) -> None:
        assert self.valid_position(position)
        self._positions[position] = None

    def place_object(self, position, obj):
        assert self.valid_position(position)
        assert not self.has_object(position)
        self._positions[position] = obj

    @staticmethod
    def obj_unparse(obj):
        if obj:
            return str(obj)
        else:
            return '-'
    
    def serialize(self):
        """Returns a unique string that represents this position."""
        return "".join([self.obj_unparse(obj) for obj in self._positions])

    def __str__(self):
        return "[ " + " ".join([self.obj_unparse(obj)
                                for obj in self._positions]) + " ]"


def test_board():
    b = Board(5)
    assert len(b.empty_positions()) == 5
    assert b.has_object(2) is False
    b.place_object(3, "X")
    assert len(b.empty_positions()) == 4
    assert 3 not in b.empty_positions()
