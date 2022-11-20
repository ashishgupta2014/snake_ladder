from typing import List


def player_move(player: str, dice_face: int, initial_pos: int, final_pos: int) -> str:
    if initial_pos != final_pos:
        message = f"{player} rolled a {dice_face} and moved from {initial_pos} to {final_pos}"
        print(message)
        return message
    message = f"{player} rolled a {dice_face} and but can't move from {initial_pos}"
    print(message)
    return message


def print_winner_name(name: str) -> str:
    message = f'{name} won the game'
    print(message)
    return message


def game_over(winner: List) -> str:
    """console output on game over"""
    print("Game Over")
    message = f'Winning Order of Players {winner}'
    print(message)
    return message
