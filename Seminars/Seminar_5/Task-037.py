# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
from random import randint

def recurs (x):
    if x == 0:
        return
    number = randint(1, 99)
    recurs(x - 1)
    print(number, end=' ')

n = 6
# n = int(input("Insert number: "))
recurs(n)