# Лямбда фунции
# def calk1(a, b):                                                              # функция
#     return a+b
calk1 = lambda a,b: a + b                                                       # лямбда функция
def calk2(a, b):
    return a*b
def math(op, x, y):
    print(op(x, y))
# math(calk1, 5, 45)
# как вызвать лямбда функцию не объявляя
math(lambda a,b: a + b, 5, 45)