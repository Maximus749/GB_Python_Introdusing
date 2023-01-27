# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

num = int(input("Введите 6- значное число: "))
first_part = num // 1000
second_part = num % 1000
first_sum = 0
second_sum = 0
for i in range(3):
    first_sum += first_part % 10
    first_part = first_part // 10
for i in range(3):
    second_sum += second_part % 10
    second_part = second_part // 10
if first_sum == second_sum:
    print("Билет счастливый")
else:
    print("Билет несчастливый")