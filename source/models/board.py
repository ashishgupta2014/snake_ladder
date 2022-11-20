from source.exception_handlers.handler import BoardValidationError
from source.models.snake import Snake
from source.models.ladder import Ladder


class Board:
    """
    Game board holds pointers to snake and ladder
    snake and ladder both has stat and position
    """
    board = dict()
    SNAKE = 'snake'
    LADDER = 'ladder'

    def __init__(self, size: int) -> None:
        self.size = size

    def _validate_board_objects(self, start: int, end: int, instance: str) -> None:
        """Validation of start and end position"""
        if start is self.size or start < 0:
            raise BoardValidationError(f'Invalid start position of {instance}')
        if end is self.size or end < 0:
            raise BoardValidationError(f'Invalid end position of {instance}')
        if start in self.board:
            raise BoardValidationError(f'The place is already occupied by another {self.board[start][0]}')

    def set_snake(self, head: int, tail: int) -> None:
        """set snakes on board"""
        self._validate_board_objects(head, tail, self.SNAKE)
        self.board[head] = (self.SNAKE, Snake(head=head, tail=tail))

    def set_ladder(self, start: int, end: int) -> None:
        """set ladders on board"""
        self._validate_board_objects(start, end, self.LADDER)
        self.board[start] = (self.LADDER, Ladder(start=start, end=end))

    def position_on_board(self, curr_pos):
        """Validate position on board and allow next moves"""
        if curr_pos > self.size:
            return -1

        if curr_pos in self.board:
            if self.board[curr_pos][0] == self.SNAKE:
                curr_pos = self.board[curr_pos][1].tail
            else:
                curr_pos = self.board[curr_pos][1].end

        return curr_pos

    def is_end_position(self, pos):
        return self.size == pos
