def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')

my_func(
    int(input('Первое число: ')),
    int(input('Первое число: ')),
    int(input('Первое число: ')),
)