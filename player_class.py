from typing import Iterable


class Player:
    def __init__(self, otherPlayers: Iterable["Player"], blankCharacter: str) -> None:
        self.name = self.getNameFromPlayer(otherPlayers)
        #self.piece = self.getPieceFromPlayer(otherPlayers, blankCharacter)



    @staticmethod
    def getNameFromPlayer(otherPlayers: Iterable["Player"]) -> str:
        """get a VALID name form the player.
        A name that is already used is invalid!!!
        """
        alreadyUsedNames = set([player.name for player in otherPlayers])
        while True:
            name = input('Please enter your name: ')
            if name not in alreadyUsedNames:
                return name
            else:
                print(f'{name} has already been used. Pick another name.')

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    pass
