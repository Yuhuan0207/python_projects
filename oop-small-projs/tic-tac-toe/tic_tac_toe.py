__author__ = "Yuhuan Fan"
"""
References:
cs1120: Introduction to Computing - http://xplorecs.org/project5
https://github.com/jeffthemaximum/python-tic-tac-toe/blob/master/tic_tac_toe.py
"""

class Player(object):
    """Class for Generic Player"""
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    def get_symbol(self):
        return self.__symbol

    def get_name(self):
        return self.__name


class HumanPlayer(Player):
    pass


class RandomPlayer(Player):
    pass


class Move(object):
    """Move on the game"""
    def __init__(self, pos: str):
        self.__position = int(pos)

    def is_valid_pos(self):
        return 0 < self.__position < 10

    def get_pos(self):
        return self.__position


class Board:
    """Class for Generic Board"""

    def __init__(self, n):
        self.size = n
        self.tiles = [["" for i in range(n)] for j in range(n)]
        self.blank_slot = n * n

    def print_board(self):
        for line in self.tiles:
            print(line)

    def move_to_coordinate(self, next_move: Move) -> (int, int):
        assert isinstance(next_move, Move)
        assert next_move.is_valid_pos()
        y = (next_move.get_pos() - 1) // self.get_board_len()
        x = (next_move.get_pos() - 1) % self.get_board_len()
        return y, x

    def get_board_len(self):
        return self.size

    def place_node(self, player, move):
        raise NotImplementedError("Generic Board cannot join the game.")


class TicTacToeBoard(Board):
    """Class for Tic Tac Toe Board"""
    def __init__(self):
        super().__init__(3)

    def get_object(self, y, x):
        return self.tiles[y][x]

    def place_node(self, player: Player, move) -> bool:
        if not move.is_valid_pos():
            print("Invalid position. Please try another move.")
            return False
        else:
            symbol = player.get_symbol()
            y, x = self.move_to_coordinate(move)
            print(f"Coordinates: ({y},{x})")
            self.tiles[y][x] = symbol
            self.blank_slot -= 1
            return True


class Game:
    """
        Class for the game.
        1. init board and players
        2. greet the players
        3. start the game
            - print current board
            - check game status
                - print out result, end game
                - ask for player input
    """

    def __init__(self, tt_board, player_1, player_2):
        self.__board = tt_board
        self.__players = [player_1, player_2]

    @staticmethod
    def initial_greeting():
        print(
            """
            Welcome to 
            
             /$$$$$$$$ /$$                 /$$$$$$$$                        /$$$$$$$$                 
            |__  $$__/|__/                |__  $$__/                       |__  $$__/                 
               | $$    /$$  /$$$$$$$         | $$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ 
               | $$   | $$ /$$_____/         | $$ |____  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$
               | $$   | $$| $$               | $$  /$$$$$$$| $$               | $$| $$  \ $$| $$$$$$$$
               | $$   | $$| $$               | $$ /$$__  $$| $$               | $$| $$  | $$| $$_____/
               | $$   | $$|  $$$$$$$         | $$|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$$
               |__/   |__/ \_______/         |__/ \_______/ \_______/         |__/ \______/  \_______/
            """)

    def greet_user(self):
        """Ask for player's move.'"""
        # select user
        moves_left = self.__board.blank_slot
        player_idx = moves_left % 2 - 1
        player = self.__players[player_idx]

        # greet user and ask for input
        next_move = input(f"Hi, {player.get_name()}. Please make your move:")
        return player, Move(next_move)

    def get_game_status(self):
        """Get game status"""
        winner = ""

        for i in range(self.__board.get_board_len()):
            # horizontal win
            if self.__board.get_object(i, 0) == self.__board.get_object(i, 1) == self.__board.get_object(i, 2) != "":
                winner = self.__board.get_object(i, 0)
                break
            # vertical win
            elif self.__board.get_object(0, i) == self.__board.get_object(1, i) == self.__board.get_object(2, i) != "":
                winner = self.__board.get_object(i, 0)
                break
            # diagonal win
            elif self.__board.get_object(0, 0) == self.__board.get_object(1, 1) == self.__board.get_object(2, 2) != "":
                winner = self.__board.get_object(0, 0)
                break
            elif self.__board.get_object(0, 2) == self.__board.get_object(1, 1) == self.__board.get_object(2, 0) != "":
                winner = self.__board.get_object(0, 2)
                break

        if winner:
            return f"Game over! {winner} is the winner!"
        else:
            if self.__board.blank_slot == 0:
                return "Game over! No one wins."
            else:
                return "Game continues..."

    def print_board(self):
        self.__board.print_board()

    def place_node_on_board(self, player, next_move):
        self.__board.place_node(player, next_move)

    def play(self):
        self.initial_greeting()
        # self.__board.print_board()
        game_status = self.get_game_status()

        while game_status == "Game continues...":
            print(game_status)
            self.print_board()
            player, next_move = self.greet_user()
            self.place_node_on_board(player, next_move)
            game_status = self.get_game_status()

        self.print_board()
        print(game_status)
        return


if __name__ == "__main__":
    board = TicTacToeBoard()
    # player1 = HumanPlayer("Katie", "X")
    # player2 = HumanPlayer("Grace", "O")
    name1 = input("Hi, Player1. What's your name?")
    symbol1 = input(f"{name1}, what symbol would you like to use?")
    name2 = input("Hi, Player2. What's your name?")
    symbol2 = input(f"{name2}, what symbol would you like to use?")
    player1 = Player(name1, symbol1)
    player2 = Player(name2, symbol2)
    new_game = Game(board, player1, player2)
    new_game.play()

