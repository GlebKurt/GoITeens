from time import sleep
from random import randint
from datetime import datetime

cells = {
    "num7": [" ", 7],
    "num8": [" ", 8],
    "num9": [" ", 9],

    "num4": [" ", 4],
    "num5": [" ", 5],
    "num6": [" ", 6],

    "num1": [" ", 1],
    "num2": [" ", 2],
    "num3": [" ", 3]
}

# numpad_keys = {
#     7: "num7",
#     8: "num8",
#     9: "num9",
#
#     4: "num4",
#     5: "num5",
#     6: "num6",
#
#     1: "num1",
#     2: "num2",
#     3: "num3"
# }

stats = []

game_running = False
win = False
gamemode_1 = False
gamemode_2 = False
is_pc_move = False

player_now = "X"
choice = None
pc_figure = None
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

numpad = True

x_wins = 0
o_wins = 0
draws = 0


# def write_in_file():
#     with open("logs.txt", "a") as file:
#         file.write(
#             f'[{current_time}] Wins X: {x_wins}. Wins O: {o_wins}. Draws: {draws}.   Gamemode: {"PvP" if gamemode_1 == True else "PvC    Player: {figure}"}\n')


def render_field():
    print(f"{cells['num7'][0]} | {cells['num8'][0]} | {cells['num9'][0]}")
    print("---------")
    print(f"{cells['num4'][0]} | {cells['num5'][0]} | {cells['num6'][0]}")
    print("---------")
    print(f"{cells['num1'][0]} | {cells['num2'][0]} | {cells['num3'][0]}\n")


def change_player():
    global player_now
    if player_now == "X":
        player_now = "O"
    else:
        player_now = "X"


def check_win():
    global player_now, win
    winning_combinations = [
        [cells["num7"], cells["num8"], cells["num9"]],  # X
        [cells["num7"], cells["num8"], cells["num9"]],
        [cells["num7"], cells["num8"], cells["num9"]],

        [cells["num7"], cells["num4"], cells["num1"]],  # Y
        [cells["num8"], cells["num5"], cells["num2"]],
        [cells["num9"], cells["num6"], cells["num3"]],

        [cells["num7"], cells["num5"], cells["num3"]],  # Diagonal
        [cells["num9"], cells["num5"], cells["num1"]]
    ]

    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] == player_now:
            stats.append(player_now)
            print(f"{player_now} виграв!")
            win = True
            return

    if all(cell != " " for row in [cells] for cell in row):
        stats.append("draw")
        print(f"Нічия!")
        win = True


def player_move():
    while True:
        choice = int(
            input(f"Зараз ходить {player_now}!\nВиберіть клітину {"(NumPad 7-3)" if numpad == True else "(1-9)"}: \n"))

        if numpad:
            if cells[f"num{choice}"][0] == " ":
                cells[f"num{choice}"][0] = player_now
            else:
                print("\nЦя клітина вже зайнята, виберіть іншу.\n")

            render_field()
        else:
            if cells[f"num{choice}"][0] == " ":
                cells[f"num{choice}"][0] = player_now
            else:
                print("\nЦя клітина вже зайнята, виберіть іншу.\n")

            render_field()


def pc_move():
    for i in range(1, 4):
        if cells[f"num{i}"][0] == cells[f"num{i + 3}"][0] == pc_figure and cells[f"num{i + 6}"][0] == " ":
            cells[f"num{i + 6}"] = pc_figure
            print(1)
            return
        elif cells[f"num{i + 3}"][0] == cells[f"num{i + 6}"][0] == pc_figure and cells[f"num{i}"][0] == " ":
            cells[f"num{i}"] = pc_figure
            print(2)
            return
        elif cells[f"num{i}"][0] == cells[f"num{i + 6}"][0] == pc_figure and cells[f"num{i + 3}"][0] == " ":
            cells[f"num{i}"][0] = pc_figure
            print(3)
            return

    while True:
        choice = randint(1, 9)

        if cells[f"num{choice}"][0] == " ":
            cells[f"num{choice}"][0] = pc_figure
            print("Random")
            return


while True:
    print("Вітаю в грі \"Хрестики нулики\"!")
    sleep(1)
    print(f"\nВ грі можна грати з комп'ютером або вдвох.\n\nПравила прості:\nВи вводите номер клітини в яку хочете "
          f"поставити свою фігуру (1 - 9 або 7 - 3)")
    input("Натисніть Enter щоб продовжити...")

    numpad = input("Виберіть режим:\n1 - NumPad\n2 - Числовий рядок\n")
    numpad = True if numpad == '1' else False if numpad == '2' else None
    while numpad is None:
        numpad = input("Невірний вибір! Будь ласка, введіть 1 або 2.")
        numpad = True if numpad == '1' else False if numpad == '2' else None
    sleep(1)

    gamemode = input("Виберіть режим гри:\nВдвох - 1\nЗ комп'ютером - 2\n")
    gamemode = 1 if gamemode == '1' else 2 if gamemode == '2' else None
    while gamemode is None:
        gamemode = input("Невірний вибір! Будь ласка, введіть 1 або 2.")
        gamemode = 1 if gamemode == '1' else 2 if gamemode == '2' else None
    sleep(1)

    while gamemode == 1:
        render_field()
        player_move()
        check_win()
        if win:
            choice = input("Ви бажаєте зіграти ще раз?").lower()
            if choice == "так":
                cells_1 = [" ", " ", " "]
                cells_2 = [" ", " ", " "]
                cells_3 = [" ", " ", " "]
                win = False
                continue
            else:
                gamemode = 0
        change_player()
