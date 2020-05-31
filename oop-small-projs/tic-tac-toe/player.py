class Player:
    """
        Generic game player - base class for any player
    """

    def __init__(self, name, mark):
        self.__name = name
        self.__mark = mark

    def get_mark(self):
        return self.__mark

    def get_name(self):
        return self.__name

    def switch_player(self, state):
        raise NotImplementedError("Generic Player doesn't know how to play!")

    def __str__(self):
        return f"Generic Player: {self.name}"