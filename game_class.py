from typing import Iterable, Set, Tuple, Dict, List
import sys
from player_class import Player
from board_class import Board
from ship_class import Ship

class Game:
    def __init__(self, numRows: int, numCols: int, blankChar: str = '*', possibleTotalHits: int = None) -> None:
        self.blankChar = blankChar
        self.possibleTotalHits = None  # this will obviously need to change to what is included in config. file
        self.board = Board(numRows, numCols, blankChar)
        self.players = []
        for playerNum in range(2):
            self.players.append(Player(self.players))
            print(self.players)
        self._curPlayerTurn = 0

    def play(self) -> None:
        while not self.someoneWon():
            self.displayGameState()
            cur_player = self.getCurPlayer()
            cur_player.takeTurn(self.board)
            self.changeTurn()
        self.displayTheWinner()
        # someone_won will remain false until hits = counter , when they equal each other, the while loop will end
        # and someone will have won the game

    def displayGameState(self) -> None:
        print('\n')
        print(self.board)

    def someoneWon(self) -> bool:
        """

        :return:
        """
        # include a counter, if hit's = counter, then somebody has won the game
        # checks each players hits. whoever has hits= counter is printed as the winner
        #
        return None

    def changeTurn(self) -> None:
        self._curPlayerTurn = (self._curPlayerTurn + 1) % 2
        # if self._cur_player_turn == 0:
        #     self._cur_player_turn = 1
        # else:
        #     self._cur_player_turn = 0

    def getCurPlayer(self) -> "Player":
        return self.players[self._curPlayerTurn]

    def displayTheWinner(self):
        if self.someoneWon():
            print(f'{self.getCurPlayer} won the game!')


if __name__ == "__main__":
    newGame = Game(10,10)
    newGame.displayGameState()
