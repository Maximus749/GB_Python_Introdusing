# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке возрастания все
# те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Input: 11 6
# Input: 2 4 6 8 10 12 10 8 6 4 2
# Input: 3 6 9 12 15 18
# Ouyput: 6 12
from random import randint

lens = input("Insert length first list: ").split()
nums1 = [randint(10, 20) for i in range(int(lens[0]))]
nums2 = [randint(10, 20) for i in range(int(lens[1]))]
print(*nums1)
print(*nums2)
my_set1 = set(nums1)
my_set2 = set(nums2)
print(*sorted(my_set1 & my_set2))
# new_set = my_set1.intersection(my_set2)
# print(*sorted(new_set))
