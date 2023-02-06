# Задача № 11
# Дано натуральное число А Ю 1. Определить каким по счету числом фиббоначи оно является.
# Ксли А не является числом фиббоначи, выведите -1

n = int(input("Введите число: "))
# n = 40
dig_1 = 0
dig_2 = 1
next = 0
count = 2
print(dig_1, dig_2, end=' ')
while dig_2 < n:
    next = dig_1 + dig_2
    dig_1, dig_2 = dig_2, next
    count += 1
    print(next, end=' ')
print()
if next == n:
    print (count)
else:
    print('-1')

