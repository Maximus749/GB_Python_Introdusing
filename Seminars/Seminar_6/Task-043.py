# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:           Вывод:
# 1 2 3 2 3       2
my_list = [1, 2, 3, 2, 3]
my_set = set(my_list)
cnt = 0
for i in my_set:
    a = my_list.count(i)
    if a == 2:
        cnt += 1
print(cnt)

# РЕШЕНИЕ НЕ МОЕ
# arr=list(int(input(f"Enter {i+1} your num:")) for i in range(int(input("Enter num len:"))))
# # arr = [1, 2, 3, 2, 3]
# print(arr)
# arr.sort()
# print(arr)
#
# count = 0
# for i in range(1, len(arr)):
#     if arr[i] == arr[i-1]:
#         count +=1
# print(count)

# РЕШЕНИЕ НЕ МОЕ
arr=[1,1,1,1,1]
n=len(arr)
result=0
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            result+=1

print(f'{arr} \n'
f'Кол-во парных элементов списка = {result}')