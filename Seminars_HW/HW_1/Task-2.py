# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите 3-значное число: "))
sum = 0
for i in range(3):
    sum += num % 10
    num = num // 10
print(sum)