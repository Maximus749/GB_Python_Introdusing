# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:                   Ввод:
# 5                       5
# 1 2 3 4 5               1 5 1 5 1
# Вывод:                  Вывод:
# 0                       2
from random import randint

# n = int(input("Insert length of list: "))
# my_list = [randint(1, 5) for _ in range(n)]
my_list = [1, 5, 1, 5, 1]
print(*my_list)
count = 0
for i in range(1, len(my_list) - 1):
    # if my_list[i] > my_list[i - 1] and my_list[i] > my_list[i + 1]:
    if my_list[i - 1] < my_list[i] > my_list[i + 1]:
        count += 1
print(count)

# РЕШЕНИЕ НЕ МОЕ
# n = 5
# numm_list = [1, 5, 1, 5, 1]
#
# count = 0
# for i in range(len(numm_list)-2):
#     test_trio = numm_list[i:i+3]
#     if test_trio[0] < test_trio[1] > test_trio[2]:
#         count += 1
# print(count)