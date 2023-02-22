# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и
# составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# new_list = []
# for i in range(len(my_list)):
#     if my_list[i] % 2 == 0:
#         new_list.append((my_list[i], my_list[i] ** 2))
# print(new_list)
# my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# new_list = []
# for i in my_list:
#     if i % 2 == 0:
#         new_list.append((i, i ** 2))
# print(new_list)

my_list = [1, 2, 3, 5, 8, 15, 23, 38]
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# res = select(int, my_list)
res = map(int, my_list)                                                         # заменили функцию select на map

# print(res)
# res = where(lambda x: x % 2 == 0, res)
res = filter(lambda x: x % 2 == 0, res)                                           # заменили функцию where на filter
# print(res)
# res = list(select(lambda x: (x, x**2), res))
res = list(map(lambda x: (x, x**2), res))                                       # заменили функцию select на map
print(res)
