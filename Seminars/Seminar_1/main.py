# Задача №1. Решение в группах
# Seminar_1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2
import math

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
# print(math.ceil(m / n))
# print(m//n + (m//n)%n)
def arg (n, m):
    return (m + n - 1) // n
res = arg(n, m)
print(res)


