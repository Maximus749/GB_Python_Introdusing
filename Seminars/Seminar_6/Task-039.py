# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
# Вывод:
# 3 3 2 12

def create_array():
    array_len = int(input("Insert length of list: "))
    new_list = [int(input("Insert list_element: ")) for _ in range(array_len)]
    return new_list
list_1 = create_array()
list_2 = create_array()
print(list_1)
print(list_2)
for i in list_1:
    if i not in list_2:
        print(i, end=' ')

# КОД НЕ МОЙ
list1 = [int(input(f'Введите {i + 1}-е число: ')) for i in
         range(int(input('Введите количество элементов первого массива: ')))]
list2 = [int(input(f'Введите {j + 1}-е число: ')) for j in
         range(int(input('Введите количество элементов второго массива: ')))]
new_list = [el for el in list1 if not (el in list2)]
print(new_list)