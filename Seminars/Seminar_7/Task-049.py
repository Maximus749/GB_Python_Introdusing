# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты
# не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато
# искусственные спутники были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой
# далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел -
# полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные
# выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# my_square = list(map(lambda x, y: x * y * 3.14, orbits))
# S = pi*a*b,
# def find_farthest_orbit(list):
#     my_square = []
#     max = 0
#     for i in range(len(orbits)):
#         if orbits[i][0] == orbits[i][1]:
#             continue
#         else:
#             S = 3.14 * orbits[i][0] * orbits[i][1]
#             my_square.append({S: orbits[i]})
#             if S > max:
#                 max = S
#     for i in my_square:
#         for key in i:
#             if key == max:
#                 return i[key]
    # return my_square
# def find_farthest_orbit(list):
#     my_square = []
#     max = 0
#     for i in orbits:
#         if i[0] == i[1]:
#             continue
#         else:
#             S = 3.14 * i[0] * i[1]
#             my_square.append({S: i})
#             if S > max:
#                 max = S
#     print(my_square)
#     for i in my_square:
#         for key in i:
#             if key == max:
#                 return i[key]
# print(find_farthest_orbit(orbits))

                                                                                # From Алексей Замараев
from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# orbits = [i for i in orbits if i[0] != i[1]]
# max_square = max([pi * i[0] * i[1] for i in orbits])
# max_square_a_b = [i for i in orbits if pi * i[0] * i[1] == max_square]
# print(max_square_a_b)

                                                                                # from Rostislav:
maximum = max(list(map(lambda x:pi*x[0]*x[1] ,(filter(lambda i: i[0]!=i[1], orbits)))))
far = filter(lambda y:pi*y[0]*y[1] == maximum, orbits)
print(*list(far))