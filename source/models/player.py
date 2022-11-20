from pydantic import BaseModel

from source.models.board import Board
from source.models.dice import Dice
from source.display.console import player_move


class Player(BaseModel):
    """Player description"""
    name: str
    position: int = 0
    status: bool = False

    def play(self, dice: Dice, board: Board):
        """Calculate Position of the player"""
        curr_pos = self.position
        curr_score = dice.roll_dice()
        new_pos = curr_pos + curr_score
        new_pos = board.position_on_board(new_pos)
        if new_pos != -1:
            self.position = new_pos
        else:
            new_pos = curr_pos
        return player_move(self.name, curr_score, curr_pos, new_pos)

    def get_status(self) -> bool:
        """current status of the player"""
        return self.status

    def set_status(self, status: bool) -> None:
        """Set status of the player from running game"""
        self.status = status
