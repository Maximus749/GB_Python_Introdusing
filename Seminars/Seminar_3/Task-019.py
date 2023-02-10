# Задача №19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# k = int(input("Введите число К: "))
# for i in range(k):
#     my_list.append(my_list[0])
#     my_list.remove(my_list[0])
# print(my_list)

your_list = [int(input('type element: ')) for i in range(int(input("insert lenght: ")))]
k = int(input("insert K: ")) % len(your_list)
print(your_list)
k_list = your_list[k:] + your_list[:k]
print(k_list)