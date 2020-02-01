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
        for shipSize in returnedDictOfShips.values():  # create a ship object with those attributes and store it in a list
            sum += shipSize
        return sum

    def play(self) -> None:  # game loop that handles playing the game
        self.possibleTotalHits = self.getMaxHits()
        print(self.possibleTotalHits)  # EXPECT FUCKING 5
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

    def takeShips(
            self):  # asks player for locations and orientation for each ship, and checks boundaries as player enters location
        for player in self.players:
            for ship in range(len(player.listOfPlayerShips)):
                player.overlappingShips = []
                player.listOfPlayerShips[ship].shipLetter = player.listOfPlayerShips[ship].shipName[0]

                orientationInput = input(f"{player.name}, what direction would you like to place {player.listOfPlayerShips[ship].shipName}? Enter 'h' for horizontal or 'v' for vertical: ")
                while orientationInput[0].lower() != 'v' and orientationInput[0].lower() != 'h':
                    orientationInput = input(f"{orientationInput} does not represent an Orientation")
                player.listOfPlayerShips[ship].orientation = orientationInput[0].lower()

                while True:  # loop until we get valid input for ship placement coordinates
                    try:
                        userInput = input(f"{player.name}, please give coordinates, separated by a comma, formatted row, column, for your {player.listOfPlayerShips[ship].shipName} of size {player.listOfPlayerShips[ship].shipSize}: ")
                        ex, ey = userInput.split(',')
                        x, y = int(ex), int(ey)
                    except ValueError:
                        print(f"{userInput} is not in the form x, y")
                        continue
                    break
                
                if player.listOfPlayerShips[ship].orientation == 'v':
                    while (x + player.listOfPlayerShips[ship].shipSize - 1) > self.maxX:
                        x = int(input(f"Please enter a value for x that is within 0 and {self.maxX}: "))
                elif player.listOfPlayerShips[ship].orientation == 'h':
                    while (y + player.listOfPlayerShips[ship].shipSize - 1) > self.maxY:
                        y = int(input(f"Please enter a value for y that is within 0 and {self.maxY}: "))
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

            for row in range(len(player.playerBoard.contents)):
                for col in range(len(player.playerBoard.contents[row])):
                    if player.playerBoard.contents[row][col] != player.playerBoard.blankChar:
                        player.playerBoard.lettersOnBoard.append(player.playerBoard.contents[row][col])
            print(player.playerBoard.lettersOnBoard)

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
