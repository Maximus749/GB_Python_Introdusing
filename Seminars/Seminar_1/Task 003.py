# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
import math
a = int(input("Введите количество детей в 1 классе: "))
b = int(input("Введите количество детей в 2 классе: "))
c = int(input("Введите количество детей в 3 классе: "))
res = (math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2))
print(res)

def arg(num):
    return num // 2 + num % 2