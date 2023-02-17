# Функции, рекурсия, алгоритмы
#import modul1              # modul1.max1 для вызова функции
from modul1 import *        # max1       для вызова функции
from random import randint

# ФУНКЦИИ
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     # print(summa)
#     return summa
# # sum_numbers(5)
# print(sum_numbers(6))
#
# def sum_str(*args):         # * звездочка означает что можно использовать много
#     res = ''                #                                       аргументов
#     for i in args:
#         res += i
#     return res
# print(sum_str('M', 'a', 'x'))

# print(max1(41, 7))
#------------------------------------------------------------------------------
# РЕКУРСИЯ
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n -2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(*list_1)
#==============================================================================
# АЛГОРИТМЫ
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# nums = [randint(1, 50) for i in range(50)]
# print(nums)
# print(quick_sort((nums)))
# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))
#------------------------------------------------------------------------------
def merge_sort(nums):                               # СОРТИРОВКА СЛИЯНИЕМ
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1, 8, 8, 6, 68, 90, 86, 34, 2, 8]
print(list1)
merge_sort(list1)
print(list1)

