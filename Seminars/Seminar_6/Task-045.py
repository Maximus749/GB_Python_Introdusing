# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа. По данному числу k
# выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5 .
# Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:           Вывод:
# 300             220 284

k = int(input('Введите число k: '))

sum_dict = dict()
for i in range(1, k + 1):
    sum_dict[i] = 1
    for j in range(2, (i // 2) + 1):
        if i % j == 0:
            sum_dict[i] += j

for i in range(1, len(sum_dict) + 1):
    for j in range(i + 1, len(sum_dict) + 1):
        if i == sum_dict[j] and j == sum_dict[i]:
            print(i, j)

# k = int(input('Введите число <= 100000: '))
# while k > 100000:
# # k = int(input('Введите число <= 100000: '))
#     list1 = []
#     liss = []
#     summa = 0
#     i = 2
#     j = 1
#     while i <= k:
#         while j < i:
#             if i % j == 0:
#                 summa += j
#                 j += 1
#             if summa > 1 and summa != k and i != summa:
#                 list1.append([i, summa])
#         summa = 0
#         i += 1
#         j = 1
#
#     i = 0
#     while i < len(list1):
#         if list1.count([list1[i][1], list1[i][0]]) > 0:
#             liss.append(list1[i])
#             i += 1
#
#     i = 0
#     while i < len(liss):
#         if liss.count([liss[i][0], liss[i][1]]) > 0:
#             del liss[i]
#         i += 1
#
#     for el in liss:
#         el.sort()
#         for l in el:
#             print(l, end=' ')
#     print()