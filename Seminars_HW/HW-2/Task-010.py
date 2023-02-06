# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# input 5 -> 1 0 1 1 0
# output 2
from random import randint

n = int(input("Ввелите количество монет: "))
coins = []
count = 0
for i in range(n):
    coins.append(randint(0, 1))
    if coins[i] == 0:
        count += 1
print(coins, end=' --> ')
if count < n - count:
    print(count)
else:
    print(n - count)
