class GameState:
    """
    Generic game state module. Do not implement any particular game.
    An actual game will need to create a subclass of GameState
    and implement the methods.
    """
    def __init__(self):
        pass

    def make_move(self, player, move):
        raise NotImplementedError("No generic update implemented!")

    def is_legal_move(self, player, move):
        raise NotImplementedError("No generic update implemented!")

    def game_over(self):
        raise NotImplementedError("No generic update implemented!")

    def outcome(self):
        raise NotImplementedError("No generic update implemented!")

    def serialize(self):
        raise NotImplementedError("No generic update implemented!")

    def __str__():
        return "<Generic Game State>"
