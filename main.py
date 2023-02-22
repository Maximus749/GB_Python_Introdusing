def create_list(n):
    while True:
        coll = list(map(int, input(f"Введите через пробел {n} элементов: ").split()))

        if n > len(coll):
            continue
            # return (f"Добавьте еще {n - len(coll)} элементов")
        elif n < len(coll):
            coll = (coll[:n])
        break
    return coll
