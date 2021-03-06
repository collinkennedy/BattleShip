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
        self._curPlayerTurn = 0

    def getMaxHits(self):
        sum = 0
        returnedDictOfShips = Ship.readFileShips()
        for shipSize in returnedDictOfShips.values():  # create a ship object with those attributes and store it in a list
            sum += shipSize
        return sum

    def play(self) -> None:  # game loop that handles playing the game
        curPlayer = None
        for playerNum in range(2):
            self.players.append(Player(self.players, self.board))
            self.players[playerNum].getListOfShips()
            curPlayer = self.getCurPlayer()
            self.takeShips()
            self.changeTurn()
        self.possibleTotalHits = self.getMaxHits()
        outerCheck = False
        while not self.someoneWon(outerCheck):
            curPlayer = self.getCurPlayer()
            print("{}'s Scanning Board".format(curPlayer.name))
            print(curPlayer.scanningBoard)
            print("{}'s Board".format(curPlayer.name))
            print(curPlayer.playerBoard)
            curPlayer.move(curPlayer, self.getOtherPlayer())
            print(f"{curPlayer.name}'s Scanning Board\n{curPlayer.scanningBoard}\n{curPlayer.name}'s Board\n{curPlayer.playerBoard}\n", end='')
            if (curPlayer.hitCounter == self.possibleTotalHits):
                outerCheck = True
                self.someoneWon(outerCheck)
                continue
            self.changeTurn()
        self.displayTheWinner(curPlayer)

        # someoneWon will remain false until hits = counter , when they equal each other, the while loop will end
        # and someone will have won the game

    def takeShips(self):  # asks player for locations and orientation for each ship, and checks boundaries as player enters location
        #for player in self.players:
        player = self.getCurPlayer()
        for ship in range(len(player.listOfPlayerShips)):
            print(f"{player}'s Placement Board\n{player.playerBoard}", end='')

            player.overlappingShips = []
            player.listOfPlayerShips[ship].shipLetter = player.listOfPlayerShips[ship].shipName[0]

            orientationInput = input(f"{player.name} enter horizontal or vertical for the orientation of {player.listOfPlayerShips[ship].shipName} which is {player.listOfPlayerShips[ship].shipSize} long: ")
            while orientationInput[0].lower() != 'v' and orientationInput[0].lower() != 'h':
                orientationInput = input(f"{orientationInput} does not represent an Orientation")
            player.listOfPlayerShips[ship].orientation = orientationInput[0].lower()

            while True:  # loop until we get valid input for ship placement coordinates
                try:
                    userInput = input(f"{player.name}, enter the starting position for your {player.listOfPlayerShips[ship].shipName} ship ,which is {player.listOfPlayerShips[ship].shipSize} long, in the form row, column: ")
                    ex, ey = userInput.split(',')
                    x, y = int(ex), int(ey)
                    if x < 0 or y < 0:
                        print("row or col were less than zero")
                        x, y = None, None
                        continue
                    break
                except ValueError:
                    print(f"{userInput} is not in the form row, col")
                    continue
                break
                
            if player.listOfPlayerShips[ship].orientation == 'v':
                while True:
                    try:
                        while (x + player.listOfPlayerShips[ship].shipSize - 1) > self.maxX:
                            entx = input(f"Please enter a value for x that is within 0 and {self.maxX - player.listOfPlayerShips[ship].shipSize + 1}: ")
                            x = int(entx)
                        while y > self.maxY:
                            enty = input(f"Please enter a value for y that is within 0 and {self.maxY}: ")
                            y = int(enty)
                        break
                    except ValueError:
                        print("Value error")
                        continue
            elif player.listOfPlayerShips[ship].orientation == 'h':
                while True:
                    try:
                        while (y + player.listOfPlayerShips[ship].shipSize - 1) > self.maxY:
                            enty = input(f"Please enter a value for y that is within 0 and {self.maxY - player.listOfPlayerShips[ship].shipSize + 1}: ")
                            y = int(enty)
                        while x > self.maxX:
                            entx = input(f"Please enter a value for x that is within 0 and {self.maxX}: ")
                            x = int(entx)
                        break
                    except ValueError:
                        print("Value error")
                        continue
            while player.playerBoard.badValues(player.listOfPlayerShips[ship], x, y, player.playerBoard, self.maxX, self.maxY, player):
                ex, ey = input(f"Please enter a new set of coordinates that do not overlap with another ship {player.overlappingShips}: ").split(",")
                x, y = int(ex), int(ey)
                if player.listOfPlayerShips[ship].orientation == 'v':
                    while (int(x) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxX:
                        enteredX = input(f"Please enter a value for x that is within 0 and {self.maxX}: ")
                        x = int(enteredX)
                        print(x, y)
                    while (int(y)) > self.maxY:
                        enteredY = input(f"Please enter a value for y that is within 0 and {self.maxY}: ")
                        y = int(enteredY)
                        print(x, y)
                elif player.listOfPlayerShips[ship].orientation == 'h':
                    while (int(y) + player.listOfPlayerShips[ship].shipSize - 1) > self.maxY:
                        enteredY = input(f"Please enter a value for y that is within 0 and {self.maxY}: ")
                        y = int(enteredY)
                        print(x, y)
                    while (int(x)) > self.maxX:
                        enteredX = input(f"Please enter a value for x that is within 0 and {self.maxX}: ")
                        x = int(enteredX)
                        print(x, y)
            player.playerBoard.placeShip(player.listOfPlayerShips[ship], int(x), int(y), player.playerBoard)
            player.playerBoard.shipsOnBoard[player.listOfPlayerShips[ship].shipName] = player.listOfPlayerShips[ship].shipSize
            player.playerBoard.UNCHANGEDSHIPSONBOARD = copy.copy(player.playerBoard.shipsOnBoard)
            #print(f"{player.name}'s Placement Board")
            #print(player.playerBoard)
            #print(player.playerBoard.shipsOnBoard) #prints dict of ships and number of occupied spaces on board
        print(f"{player}'s Placement Board\n{player.playerBoard}", end='')

    def displayGameState(self) -> None:
        print(self.board)

    def changeTurn(self) -> None:  # switches player turn
        self._curPlayerTurn = (self._curPlayerTurn + 1) % 2

    def getCurPlayer(self) -> "Player":  # returns current player
        return self.players[self._curPlayerTurn]

    def getOtherPlayer(self) -> "Player":  # returns other player
        if self.getCurPlayer() == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]

    def someoneWon(self, check: bool):
        return check

    def displayTheWinner(self, player: "Player"):
        print(f'{player} won the game!')

if __name__ == "__main__":
    pass