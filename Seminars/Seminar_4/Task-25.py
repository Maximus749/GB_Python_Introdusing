# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

# new_string = (i for i in input("insert string: ").split())
# print(type(new_string))
# s = 'aaabcaadcdd'
# print(s)
# s = s.split()
# print(type(s))
# s = 'a a a b c a a d c d d'
# s = s.split()
# # print(s)
# result_dic = {}                                 #dictionary в который будем класть счетчики какой символ сколько раз встречается
# new_s = []                                      # новый лист в который будем класть по условию в задаче
# for i in s:
#     if i not in result_dic:                     # если еще нет в словаре, первый раз
#         new_s.append(i)                         # кладем наш символ
#     # print(i)
#         result_dic[i] = result_dic.get(i, 0)+ 1 # с помощью метода get возвращаем в словарь наш символ искусственно добавляя 1
#     else:                                       # если уже есть в словаре, значит пошли повторы
#         new_s.append(f'{i}_{result_dic[i]}')    # кладем значение с постфиксом и значение из словаря
# #         # print(f'{i}_{result[i]}')
#         result_dic[i] = result_dic.get(i, 0) + 1
# print(result_dic)
# print(*new_s)

s = 'a a a b c a a d c d d'
s = s.split()
print(s)
new_dict = {}
for i in s:
    if i not in new_dict:
        print(i, end=' ')
        new_dict[i] = new_dict.get(i, 0) + 1
    else:
        print((f"{i}_{new_dict[i]}"), end=' ')
        new_dict[i] = new_dict.get(i, 0) + 1