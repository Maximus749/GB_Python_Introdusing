# Задача 24:
#   В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке
# растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени
# сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#     В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
#     Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4 -> 1 2 3 4
# Ouyput: 9
from random import randint

amount_of_bush = int(input("Введите количество кустов: "))
bushs = [randint(3, 10) for i in range(amount_of_bush)]
print(bushs)
count_of_berries = dict()
for i in range(len(bushs)):
    if i == 0:
        count_of_berries[i + 1] = bushs[i] + bushs[i+1] + bushs[-1]
    elif i == len(bushs) - 1:
        count_of_berries[i + 1] = bushs[i] + bushs[i - 1] + bushs[0]
    else:
        count_of_berries[i + 1] = bushs[i] + bushs[i - 1] + bushs[i + 1]
print(count_of_berries)
max_amount = 0
max_amount_key = 0
for i in count_of_berries:
    if count_of_berries[i] > max_amount:
        max_amount = count_of_berries[i]
        max_amount_key = i
# print(max_amount_key, max_amount)
if max_amount_key == 1:
    print(f"Больше всего ягод можно собрать с 1, 2 и \
{amount_of_bush + 1} кустов")
elif max_amount_key == amount_of_bush + 1:
    print(f"Больше всего ягод можно собрать с 1, \
{amount_of_bush} и {amount_of_bush + 1} кустов")
else:
    print(f"Больше всего ягод можно собрать с {max_amount_key - 1},\
{max_amount_key} и {max_amount_key + 1} кустов")