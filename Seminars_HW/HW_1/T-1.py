import math
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#-----------------------------------------------------------------------------------------------------------------------

day = int(input("Введите цифру обозначающюю день недели: "))
if day >= 1 and day <= 5:
    print("Это будний день")
elif day >5 and day < 8:
        print("Это выходной!!!")


#=======================================================================================================================
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#=======================================================================================================================
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#-----------------------------------------------------------------------------------------------------------------------

x = int(input("Введите координату х: "))
y = int(input("Введите координату y: "))
if x > 0 and y > 0:
    print("Точка находится в 1 четверти.")
elif x > 0 and y < 0:
    print("Точка находится в 2 четверти.")
elif x < 0 and y < 0:
    print("Точка находится в 3 четверти.")
elif x < 0 and y > 0:
    print("Точка находится в 4 четверти.")

#=======================================================================================================================
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).
#-----------------------------------------------------------------------------------------------------------------------

quarter = int(input("Введите номер четверти: "))
if quarter == 1:
    print("Точка в 1 четверти может иметь координаты Х от 0 до бесконечности, У от 0 до бесконечности")
elif quarter == 2:
    print("Точка во 2 четверти может иметь координаты Х от 0 до бесконечности, У от 0 до '-' бесконечности")
elif quarter == 3:
    print("Точка в 3 четверти может иметь координаты Х от 0 до '-' бесконечности, У от 0 до '-' бесконечности")
elif quarter == 4:
    print("Точка в 4 четверти может иметь координаты Х от 0 до '-' бесконечности, У от 0 до бесконечности")

#=======================================================================================================================
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
#-----------------------------------------------------------------------------------------------------------------------
x1 = int(input("Введите координату х1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату х2: "))
y2 = int(input("Введите координату y2: "))

distance = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print(round(distance, 2))