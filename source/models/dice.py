import random


class Dice:
    """Dice Description"""

    def __init__(self, on_of_dice: int = 1) -> None:
        self.on_of_dice = on_of_dice
        self.faces = 6

    def roll_dice(self) -> int:
        """Rolling Dice and get random number"""
        score = 0
        possible_max_move = 3
        while possible_max_move:
            possible_max_move -= 1
            dice = self.on_of_dice
            rolling_score = 0
            while dice:
                rolling_score += random.randint(1, self.faces)
                dice -= 1
            if rolling_score != self.faces*self.on_of_dice:
                return score + rolling_score
            score += rolling_score
        return 0
