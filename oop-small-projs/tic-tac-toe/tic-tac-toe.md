# Tic Tac Toe - OOP Design

## Overview
- `game.py` — Defines the Game class for playing two-player, perfect information, turn-based games.
- `board.py` — Defines the Board class for representing a simple board with no structure or game rules.
- `squareboard.py` — Defines the SquareBoard class, a subclass of Board, for representing a square board where the positions can be referenced with a Position object (also defined by a class in this file) which contains two coordinates.
- `tictactoe.py` — Defines the TicTacToeBoard class, a subclass of SquareBoard, for playing games of Tic-Tac-Toe.
- `player.py` — Defines a generic Player class.
- `humanplayer.py` — Defines a HumanPlayer class, a subclass of Player, that uses user input to select moves.
- `randomplayer.py` — Defines a RandomPlayer class, a subclass of Player, that plays (badly, for most games!) by randomly picking a legal move.
- `learningplayer.py` — Defines a LearningPlayer class, a subclass of Player, that learns to play a game based on learning from games played. Note that the learning player does not know anything about the game it is learning to play, and can be used to learn to play any move and state-based game.

## Approaches
- top down: 关注high level design，将每个module当做black box（暂不关注具体功能与实现）
- bottom up: 

1. generic `GameState` class 
   - not implement any specific game
   - base class for implementing any game
2. `Board` class implement a generic board
   - in tic tac toe, a game state can be represented with a board - containing state of every position
   - the Board has no structure - it just represents the state of the game with a flat list, with one element corresponding to each board position.
3. `SquareBoard` class to implement 2D square board, `Position` class -> 2D coordinates on square board
    




## Reference
[cs1120: Introduction to Computing ](http://xplorecs.org/project5)