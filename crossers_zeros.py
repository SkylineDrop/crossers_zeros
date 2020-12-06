def desk_mapping(desk):
    width = len(desk)
    height = len(desk[0])
    title = " | ".join(str(x) for x in range(width + 1))
    print(title, '|')

    for y in range(1, height + 1):
        row = ' | '.join(x or ' ' for x in desk[y-1])
        print(y, '|', row, '|')
    return


def check_win_conditions(desk):
    return (
        check_for_horizontal(desk)
        or check_for_diagonal(desk)
        or check_for_vertical(desk)
    )


def check_for_vertical(desk):
    result = list(zip(*desk))
    win_combination_1 = ("X", "X", "X")
    win_combination_2 = ("O", "O", "O")
    for i in range(len(result)):
        if result[i] == win_combination_1 or result[i] == win_combination_2:
            return True
    return False


def check_for_horizontal(desk):
    win_combination_1 = ["X", "X", "X"]
    win_combination_2 = ["O", "O", "O"] 
    for i in range(len(desk)):
        if desk[i] == win_combination_1 or desk[i] == win_combination_2:
            return True
    return False


def check_for_diagonal(desk):
    diag_1 = {desk[i][i] for i in range(len(desk))}
    diag_2 = {desk[len(desk) - 1 - i][i] for i in range(len(desk))}
    win_combination_1 = {"X"}
    win_combination_2 = {"O"}
    if diag_1 == win_combination_1 or diag_1 == win_combination_2:
        return True
    if diag_2 == win_combination_1 or diag_1 == win_combination_2:
        return True
    return False


def is_cell_available(desk, x, y):
    if not 0 <= x <= 2 or not 0 <= y <= 2:
        return False

    if desk[x][y] is None:
        return True
    print("This cell is taken. Reassign your move")
    return False


def player_move(desk, player):
    x = y = -1
    while not is_cell_available(desk, x, y):
        list_input = input(f'Player "{player}", choose a cell - two numbers (row, column), '
                           'separated by a space: ').split()

        if len(list_input) != 2:
            continue

        x, y = list_input
        x, y = int(x) - 1, int(y) - 1
    return x, y


def is_tie(desk):
    for row in desk:
        if None in row:
            return False
    return True


def start_game():
    print("Game engagement")
    players = ['X', 'O']
    desk = [[None for x in range(3)] for y in range(3)]
    desk_mapping(desk)
    current_player = 0
    while True:
        player_name = players[current_player]
        # ход игрока
        move_x, move_y = player_move(desk, player_name)
        desk[move_x][move_y] = player_name

        desk_mapping(desk)
        # проверка победы
        if check_win_conditions(desk):
            print(f'Player {player_name} win!')
            return

        if is_tie(desk):
            print('Nobody wins!')
            return

        # передача хода
        # чередование остатков при делении на 2
        current_player = (current_player + 1) % 2


start_game()
