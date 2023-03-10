# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли
# объекты имеют одинаковое значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов отличается -
# то False. Для пустого набора объектов, функция должна возвращать True. Аргумент
# characteristic - это функция, которая принимает объект и вычисляет его
# характеристику.
#
# Ввод:                                   Вывод:
# values = [0, 2, 10, 6]                      #same
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
#------------------------------------------------------------------------------
def same_by(characteristic, objects):                                         # My
    for i in objects:
        if characteristic(i):
            return False
    return True
#------------------------------------------------------------------------------

# def same_by(characteristic, objects):                                           # from Денис
    # if not objects:
    #     return True
    # first_value = characteristic(objects[0])
    # return all(characteristic(obj) == first_value for obj in objects)
#------------------------------------------------------------------------------

# def same_by(characteristic, objects):                                           # from Алексей Замараев:
#     for i in objects:
#         if characteristic(i):
#             return False
#     return True
#------------------------------------------------------------------------------

# def same_by(func, list1):                                                       # from Георгий
#     new_list1 = list(filter(func, list1))
#     return len(new_list1) == len(list1) or len(new_list1) == 0


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')