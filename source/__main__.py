from models.game import Game


def main():
    board_size = int(input("Enter board size: "))
    players = list(map(str, input().split()))
    no_of_dice = int(input("Enter dice count: "))

    snakes_count = int(input("Enter snakes count: "))
    snakes = []
    for i in range(snakes_count):
        snakes.append(tuple(map(int, input().split())))

    ladders_count = int(input("Enter snakes count: "))
    ladders = []
    for i in range(ladders_count):
        ladders.append(tuple(map(int, input().split())))

    # board_size = 100
    # players = ['Payal', 'Roshni', 'Kartik']
    # no_of_dice = 1
    # snakes_count = 9
    # snakes = [(62, 5), (33, 6), (49, 9), (88, 16), (41, 20), (56, 53), (98, 64), (93, 73), (95, 75)]
    # ladders_count = 8
    # ladders = [(2, 37), (27, 46), (10, 32), (51, 68), (61, 79), (65, 84), (71, 91), (81, 100)]

    snake_ladder_game = Game(no_of_dice, board_size)
    snake_ladder_game.set_players(players)
    snake_ladder_game.set_snake_ladders(snakes, ladders)
    snake_ladder_game.play_game()


if __name__ == "__main__":
    main()
