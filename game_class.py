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

    def getMaxHits(self):
        sum = 0
        returnedDictOfShips = Ship.readFileShips()
        for shipSize in returnedDictOfShips.values(): # create a ship object with those attributes and store it in a list
            sum += shipSize
        return sum

    def play(self) -> None: # game loop that handles playing the game
        self.possibleTotalHits = self.getMaxHits()
        print(self.possibleTotalHits) # EXPECT FUCKING 5
        curPlayer = self.getCurPlayer()
        self.takeShips()
        outerCheck = False
        while not self.someoneWon(outerCheck):
            curPlayer = self.getCurPlayer()
            print("{}'s Scanning Board".format(curPlayer.name))
            print(curPlayer.scanningBoard)
            print("{}'s Ship Board".format(curPlayer.name))
            print(curPlayer.playerBoard)
            curPlayer.move(curPlayer, self.getOtherPlayer())
            if (curPlayer.hitCounter == self.possibleTotalHits):
                self.displayTheWinner(curPlayer)
                outerCheck = True
                self.someoneWon(outerCheck)
            self.changeTurn()
        
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
                if player.listOfPlayerShips[ship].orientation == 'v':
                    while (int(x) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxX:
                        x = input("Please enter a value for x that is within bounds: ")
                elif player.listOfPlayerShips[ship].orientation == 'h':
                    while (int(y) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxY:
                        y = input("Please enter a value for y that is within bounds: ")
                while player.playerBoard.badValues(player.listOfPlayerShips[ship], int(x), int(y), player.playerBoard, self.maxX, self.maxY):
                    x, y = input("Please enter a new set of coordinates that do not overlap with another ship: ").split(",")
                    if player.listOfPlayerShips[ship].orientation == 'v':
                        while (int(x) + player.listOfPlayerShips[ship].shipSize - 1) > maxX:
                            enteredX = input("Please enter a value for x that is within bounds: ")
                            x = int(enteredX)
                            print(x, y)
                        while (int(y)) > maxY:
                            enteredY = input("Please enter a value for y that is within bounds: ")
                            y = int(enteredY)
                            print(x, y)
                    elif player.listOfPlayerShips[ship].orientation == 'h':
                        while (int(y) + player.listOfPlayerShips[ship].shipSize - 1) > maxY:
                            enteredY = input("Please enter a value for y that is within bounds: ")
                            y = int(enteredY)
                            print(x, y)
                        while (int(x)) > maxX:
                            enteredX = input("Please enter a value for x that is within bounds: ")
                            x = int(enteredX)
                            print(x, y)
                print(int(x), int(y))
                player.playerBoard.placeShip(player.listOfPlayerShips[ship], int(x), int(y), player.playerBoard)

    def displayGameState(self) -> None:
        print(self.board)

    def changeTurn(self) -> None: # switches player turn
        self._curPlayerTurn = (self._curPlayerTurn + 1) % 2
        
    def getCurPlayer(self) -> "Player": # returns current player
        return self.players[self._curPlayerTurn]

    def getOtherPlayer(self) -> "Player": # returns other player
        if self.getCurPlayer() == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]

    def someoneWon(self, check : bool):
        return check

    def displayTheWinner(self, player : "Player"):
        print(f'{player} won the game!')
        
if __name__ == "__main__":
    pass