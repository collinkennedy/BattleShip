from typing import Iterable, Set, Tuple, Dict, List
import sys
import copy
from player_class import Player
from board_class import Board
from ship_class import Ship

class Game:
    def __init__(self, numRows: int, numCols: int, blankChar: str = '*', possibleTotalHits: int = None) -> None:
        self.blankChar = blankChar
        self.possibleTotalHits = None  # this will obviously need to change to what is included in config. file
        self.board = Board(numRows, numCols, blankChar)
        self.players = []
        self.maxX = numRows - 1
        self.maxY = numCols - 1
        for playerNum in range(2):
            self.players.append(Player(self.players, self.board))
            print(self.players)
            self.players[playerNum].getListOfShips()
        self._curPlayerTurn = 0

    def play(self) -> None: # game loop that handles playing the game
        curPlayer = self.getCurPlayer()
        self.takeShips()
        while not self.someoneWon():
            curPlayer = self.getCurPlayer()
            print("{}'s Scanning Board".format(curPlayer.name))
            print(curPlayer.scanningBoard)
            print("{}'s Ship Board".format(curPlayer.name))
            print(curPlayer.playerBoard)
            pause = input("Press any key to loop...")
            self.changeTurn()
        self.displayTheWinner()
        # someoneWon will remain false until hits = counter , when they equal each other, the while loop will end
        # and someone will have won the game

    def takeShips(self): # asks player for locations and orientation for each ship, and checks boundaries as player enters location
         for player in self.players:
            for ship in range(len(player.listOfPlayerShips)):
                player.listOfPlayerShips[ship].shipLetter = player.listOfPlayerShips[ship].shipName[0]

                orientation = input(f"{player.name}, what direction would you like to place {player.listOfPlayerShips[ship].shipName}? Enter 'h' for horizontal or 'v' for vertical: ")[0].lower()
                while orientation != 'h' and orientation != 'v':
                    orientation = input("Please enter either 'h' for horizontal or 'v' for vertical: ")[0].lower()
                player.listOfPlayerShips[ship].orientation = orientation

                x, y = input(f"{player.name}, please give coordinates, separated by a comma, formatted row, column, for your {player.listOfPlayerShips[ship].shipName} of size {player.listOfPlayerShips[ship].shipSize}: ").split(',')
                while (int(x) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxX:
                    x = input("Please enter a value for x that is within bounds: ")
                while (int(y) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxY:
                    y = input("Please enter a value for y that is within bounds: ")
                while (player.playerBoard.badValues(player.listOfPlayerShips[ship], int(x), int(y))):
                    x, y = input("Please enter a new set of coordinates that do not overlap with another ship: ")
                player.playerBoard.placeShip(player.listOfPlayerShips[ship], int(x), int(y))

                #tempX = int(x)
                #tempY = int(y)
                #orientation = input(f"What direction would you like to place {player.listOfPlayerShips[ship].shipName}? Enter 'h' for horizontal or 'v' for vertical: ")[0].lower()
                #while orientation != 'h' and orientation != 'v':
                #    orientation = input("Please enter either 'h' for horizontal or 'v' for vertical: ")[0].lower()
                #tempOrientation = orientation
                #player.playerBoard.placeShips(player.listOfPlayerShips[ship], tempX, tempY, tempOrientation)
                print(player.listOfPlayerShips[ship].shipName)
                print(player.listOfPlayerShips[ship].placementPosX)
                print(player.listOfPlayerShips[ship].placementPosY)

            #player.playerBoard.placeShips(player.listOfPlayerShips[ship])

    def displayGameState(self) -> None:
        print(self.board)

    def someoneWon(self) -> bool:
        # include a counter, if hits = counter, then somebody has won the game
        # checks each players hits. whoever has hits= counter is printed as the winner
        return None

    def changeTurn(self) -> None: # switches player turn
        self._curPlayerTurn = (self._curPlayerTurn + 1) % 2
        
    def getCurPlayer(self) -> "Player": # returns current player
        return self.players[self._curPlayerTurn]

    def displayTheWinner(self):
        if self.someoneWon():
            print(f'{self.getCurPlayer} won the game!')

if __name__ == "__main__":
    pass