# MAP

# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем список из
# значений строки, пример:
# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
# 2. Теперь вернемся к задаче. С помощью функции map():
# data = list(map(int,input().split()))

# .split()  Преобразует строку в список, по умолчанию использует пробел как разделитель

# data = '1 2 3 5 8 15 23 38'                                                     # дана строка
# print(data)
# # data = data.split()                                                             # здесь уже список строк
# # print(data)
#
# data = list(map(int, data.split()))                                             # здесь уже список чисел
# print(data)


# функция FILTER
# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 5 == 0, data))
print(res)