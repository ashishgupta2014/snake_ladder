import unittest
from source.models.game import Game


class TestSnakeLadder(unittest.TestCase):
    """Tests for `snake_ladder` package."""

    def setUp(self):
        self.board_size = 100
        self.players = ["vaibh", "dwan"]
        self.no_of_dice = 1
        self.snakes = [(87, 23), (43, 11), (98, 56), (76, 36)]
        self.ladders = [(12, 45), (40, 60), (73, 91), (62, 81)]

        self.snake_ladder_game = Game(self.no_of_dice, self.board_size)
        self.snake_ladder_game.set_snake_ladders(self.snakes, self.ladders)
        self.snake_ladder_game.set_players(self.players)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_add_winner(self):
        expected = ["vaibh"]
        self.snake_ladder_game.add_winner("vaibh")
        assert self.snake_ladder_game.winners == expected

    def test_dice_score(self):
        assert self.snake_ladder_game.dice.roll_dice() > 0
