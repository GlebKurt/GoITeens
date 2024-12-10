import time
from random import randint

cells_1 = [" ", " ", " "]
cells_2 = [" ", " ", " "]
cells_3 = [" ", " ", " "]

stats = []

game_running = False
win = False
gamemode_1 = False
gamemode_2 = False
is_pc_move = False
pc_figure = None

player_now = "X"
choice = None

x_wins = 0
o_wins = 0
draws = 0


def render_field():
    print(f"{cells_1[0]} | {cells_1[1]} | {cells_1[2]}")
    print("---------")
    print(f"{cells_2[0]} | {cells_2[1]} | {cells_2[2]}")
    print("---------")
    print(f"{cells_3[0]} | {cells_3[1]} | {cells_3[2]}\n")


def change_player():
    global player_now
    if player_now == "X":
        player_now = "O"
    else:
        player_now = "X"


def check_win():
    global player_now, win
    winning_combinations = [  # Зробити таким способом мені підказав ChatGPT
        [cells_1[0], cells_1[1], cells_1[2]],
        [cells_2[0], cells_2[1], cells_2[2]],
        [cells_3[0], cells_3[1], cells_3[2]],

        [cells_1[0], cells_2[0], cells_3[0]],
        [cells_1[1], cells_2[1], cells_3[1]],
        [cells_1[2], cells_2[2], cells_3[2]],

        [cells_1[0], cells_2[1], cells_3[2]],
        [cells_1[2], cells_2[1], cells_3[0]]
    ]

    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] == player_now:
            stats.append(player_now)
            print(f"{player_now} виграв!")
            win = True
            return

    if all(cell != " " for row in [cells_1, cells_2, cells_3] for cell in row):
        stats.append("draw")
        print(f"Нічия!")
        win = True


def pc_move():
    while True:
        choice = randint(1, 9)

        if choice in range(1, 4) and cells_1[choice - 1] == " ":
            cells_1[choice - 1] = pc_figure
            return
        elif choice in range(4, 7) and cells_2[choice - 4] == " ":
            cells_2[choice - 4] = pc_figure
            return
        elif choice in range(7, 10) and cells_3[choice - 7] == " ":
            cells_3[choice - 7] = pc_figure
            return


print("Вітаю в грі \"Хрестики нулики\"!")
time.sleep(1)
print(f"\nВ грі можна грати з комп'ютером або вдвох.\n\nПравила прості:\nВи вводите номер клітини в яку хочете "
      f"поставити свою фігуру (1 - 9)")
input("Натисніть Enter щоб продовжити...")

while True:
    if win: break

    game_running = True
    player_now = "X"

    while True:
        gamemode = input("Виберіть режим гри:\nВдвох - 1\nЗ комп'ютером - 2\n")
        if gamemode == "1":
            game_running = True
            gamemode_1 = True
        elif gamemode == "2":
            game_running = True
            gamemode_2 = True
        else:
            print("Введене не коректне значення!")

        while gamemode_1:
            if win: break

            render_field()
            while True:
                time.sleep(1)
                choice = int(input(f"Зараз ходить {player_now}!\nВиберіть клітину (1-9): \n"))

                if choice in range(1, 4) and cells_1[choice - 1] == " ":
                    cells_1[choice - 1] = player_now
                elif choice in range(4, 7) and cells_2[choice - 4] == " ":
                    cells_2[choice - 4] = player_now
                elif choice in range(7, 10) and cells_3[choice - 7] == " ":
                    cells_3[choice - 7] = player_now
                else:
                    print("\nЦя клітина вже зайнята, виберіть іншу.\n")

                render_field()
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
                        break

                change_player()

        while gamemode_2:
            if win: break

            time.sleep(1)
            while True:
                figure = input("Введіть цифру що відповідає фігурі:\nХ - 1\nO - 2\n")
                if figure == "1":
                    figure = "X"
                    pc_figure = "O"
                    break
                elif figure == "2":
                    figure = "O"
                    pc_figure = "X"
                    break
                else:
                    print('Ви ввели не коректний номер!')

            time.sleep(1)
            render_field()
            while True:
                if player_now == figure:
                    choice = int(input(f"Зараз ходить {player_now}!\nВиберіть клітину (1-9): \n"))
                    if choice in range(1, 4) and cells_1[choice - 1] == " ":
                        cells_1[choice - 1] = player_now
                    elif choice in range(4, 7) and cells_2[choice - 4] == " ":
                        cells_2[choice - 4] = player_now
                    elif choice in range(7, 10) and cells_3[choice - 7] == " ":
                        cells_3[choice - 7] = player_now
                    else:
                        print("\nЦя клітина вже зайнята, виберіть іншу.\n")
                        continue
                elif player_now == pc_figure:
                    print("Зараз ходить О (комп'ютер)!")
                    pc_move()

                render_field()
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
                        break

                change_player()

        for wins in stats:
            if wins == "X":
                x_wins += 1
            elif wins == "O":
                o_wins += 1
            elif wins == "draw":
                draws += 1

        print(f"Статистика гри:\nВиграшів Х: {x_wins}\nВиграшів О: {o_wins}\nНічий: {draws}")
        break
