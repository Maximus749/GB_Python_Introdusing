# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

# list_length = int(input('Введите длину списка: '))
# nums = [i for i in range(1, list_length + 1)]
# print(f'Список {nums}')
# num = int(input('Введите X: '))
# for i in range(list_length):
#     if num <= 0:
#         print('Вы ввели ноль или отрицательное число, нужно ввести натуральное число')
#     elif nums[i] == num:
#         print(f'Вы ввели число из списка, это {nums[i]}')
#     elif nums[-1] < num:
#         print(f'Вы ввели {num} которого нет в списке и самое близкое число это {nums[-1]}')
#         break

my_list = [int(input('type element: ')) for i in range(int(input('type amount: ')))]
x = int(input('type X: '))
if x in my_list:
    print(x)                                                    # если х есть в изначальном списке то его и выводим
else:
    my_list.append(x)                                           # добавили в первый список значение Х
my_list = sorted(my_list)                                       # отсортировали список от меньшего к большему
if my_list.index(x) == len(my_list) - 1:                        # если искомый элемент самый большой
    element2 = my_list[my_list.index(x) - 1]                    # ближайший слева элемент к искомому
    print(element2)
elif my_list.index(x) == 0:                                     # если искомый элемент самый маленький
    element = my_list[my_list.index(x) + 1]                     # [1] ближайший справа элемент к искомому
    print(element)
else:                                                           # если искомый элемент в середине, выводим оба соседних с ним элемнта
    element = my_list[my_list.index(x) - 1]                     # ближайший слева элемент к искомому
    print(element)
    element2 = my_list[my_list.index(x) + 1]                    # ближайший справа элемент к искомому
    print(element2)