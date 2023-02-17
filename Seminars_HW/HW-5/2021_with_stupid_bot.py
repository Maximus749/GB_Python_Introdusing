from random import randint

def step(player_num, player, total):
    total -= player_num
    if total != 0:
        if player == 0:
            print(f"БОТ взял {player_num}, осталось {total}")
        else:
            print(f"Игрок (ты) взял {player_num}, осталось {total}")
    else:
        print("Выиграл игрок", player)
    return total

player = randint(0, 1)
# player = 0
total = 202
while total > 0:
    if player == 0:
        if total < 29:
            num = total
        else:
            num = randint(1, 28)
    else:
        num = int(input("Введите число от 1 до 28:"))
    step(num, player, total)
    if player == 0:
        player = 1
    else:
        player = 0
    total -= num


