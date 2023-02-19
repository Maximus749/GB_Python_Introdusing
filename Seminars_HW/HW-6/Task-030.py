# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.     an = 7 + (5 - 1) * 2
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_number = int(input("Insert first number: "))
differance =  int(input("Insert differance: "))
length_numrers =  int(input("Insert length: "))
# num = first_number                                                            # РЕШЕНИЕ № 1
# my_nums = []
# # for i in range(first_number, first_number + length_numrers, differance):
# #     my_nums.append(i)
# for i in range(length_numrers):
#     my_nums.append(num)
#     num += differance
# print(*my_nums)


nums = []                                                                       # РЕШЕНИЕ № 2 ПО ФОРМУЛЕ В УСЛОВИИ
a = first_number
n = 1
while n <= length_numrers:
    nums.append(a)
    n += 1
    a = first_number + (n - 1) * differance
print(*nums)