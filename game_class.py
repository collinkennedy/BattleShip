from board_class import Board
import game_class
from player_class import Player


class Game:
    def __init__(self, dimensions: int, blank_char: str = '*', possibleTotalHits: int = None) -> None:
        self.blank_char = blank_char
        self.possibleTotalHits = None  # this will obviously need to change to what is included in config. file
        self.board = Board(dimensions, dimensions, blank_char)
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players, blank_char))
        self._cur_player_turn = 0

    def play(self) -> None:
        while not self.someone_won():
            self.display_game_state()
            cur_player = self.get_cur_player()
            cur_player.take_turn(self.board)
            self.change_turn()
        self.display_the_winner()
        # someone_won will remain false until hits = counter , when they equal each other, the while loop will end
        # and someone will have won the game

    def display_game_state(self) -> None:
        print(self.board)

    def someone_won(self) -> bool:
        """

        :return:
        """
        # include a counter, if hit's = counter, then somebody has won the game
        # checks each players hits. whoever has hits= counter is printed as the winner
        #
        return self.someone_won_horizontally() or self.someone_won_vertically() or self.someone_won_diagonally()

    def change_turn(self) -> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2
        # if self._cur_player_turn == 0:
        #     self._cur_player_turn = 1
        # else:
        #     self._cur_player_turn = 0

    def get_cur_player(self) -> "Player":
        return self.players[self._cur_player_turn]

    def display_the_winner(self):
        if self.someone_won():
            print(f'{self.get_cur_player()} won the game!')
        else:
            print('Tie Game.')


if __name__ == "__main__":
    pass
