import sys
from typing import List

from source.display.console import print_winner_name, game_over
from source.exception_handlers.handler import BoardValidationError, GameValidationError
from source.models.player import Player
from source.models.dice import Dice
from source.models.board import Board


class Game:
    """Snake Ladder Game"""
    players = dict()

    def __init__(self, no_of_dice, board_size) -> None:
        self.winners = []
        self.dice = Dice(no_of_dice)
        self.board = Board(board_size)
        self.active_players = 0

    def set_players(self, players: List) -> None:
        """Initialize Players"""
        self.active_players = len(players)

        if self.active_players < 2:
            raise GameValidationError("Not enough Players!")

        for player in players:
            self.players[player] = Player(name=player)

    def set_snake_ladders(self, snakes: List, ladders: List) -> None:
        """Set snake and Ladder"""
        for snake in snakes:
            try:
                self.board.set_snake(*snake)
            except BoardValidationError:
                continue

        for ladder in ladders:
            try:
                self.board.set_ladder(*ladder)
            except BoardValidationError:
                continue

    def add_winner(self, winner) -> None:
        """Maintain in-memory list winning order of the player"""
        print_winner_name(winner)
        self.winners.append(winner)

    def play_game(self) -> None:
        """Run Pilot mode of the game"""
        while True:
            for _, player in self.players.items():
                if not player.get_status():
                    player.play(self.dice, self.board)
                    if self.board.is_end_position(player.position):
                        player.set_status(True)
                        self.add_winner(player.name)
                        self.active_players -= 1

                if self.active_players < 2:
                    game_over(self.winners)
                    sys.exit()
