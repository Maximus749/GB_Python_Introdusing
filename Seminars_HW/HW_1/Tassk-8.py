# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

size_n = int(input("Введите размер n: "))
size_m = int(input("Введите размер m: "))
num = int(input("Сколько кусочков вы хотите отломить?: "))
if num % size_n == 0 or num % size_m == 0:
    print("Yes")
else:
    print("No")
