def my_rectangle(y, z):
    return y * z
def my_square(q):
    return q ** 2

def all_shapes(n):
    sum_square = 0
    for i in range(n):
        fig = int(input("укажите фигуру: 1 - квадрат, 2 - прямоугольник:"))
        min_or_plus = input("Введите - или +: ")
        if fig == 1:
            square = my_square(int(input("Введите сторону квадрата: ")))
        else:
            a = int(input("Ввелите длину прямоугольника: "))
            b = int(input("Ввелите ширину прямоугольника: "))
            square = my_rectangle(a, b)
        if min_or_plus == '-':
            sum_square -= square
        else:
            sum_square += square
    return sum_square

def main():
    print("Здесь начинается основной код")
    x = 5
    print(my_square(x))
    print("Здесь начинается основной код")

if __name__ == '__main__':
    main()
