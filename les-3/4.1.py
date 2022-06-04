def my_func():
    x = float(input("Введите положительное число "))
    y = float(input("Введите отрацельное число: "))
    res = 1
    while (y<0):
        res = res * x
        y = y + 1
    res = 1 / res
    return res
print(f'{my_func()}')


