# Задача 26:
# Напишите с помощью рекурсии программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B .
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def pow_num(a, b, c):           # МОЕ РЕШЕНИЕ
#     if b == 1:
#         return a
#     a *= c
#     return pow_num(a, b - 1, c)
#
# num1 = 2
# num2 = 3
# num3 = num1
# print(pow_num(num1, num2, num3))

# Не мое решение
def exponent(a,b):
    if b == 0:
        a = 1
        return a
    elif b == 1 :
        return a
    return a * exponent(a, b-1)
print(exponent(3, 5))
