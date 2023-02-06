# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
#
# 10 -> 1 2 4 8

n = int(input("Введите число: "))
result = 0
i = 0
while result < n:
    result = 2 ** i
    if result < n:
        print(result)
    i += 1