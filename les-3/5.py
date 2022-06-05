def sum ():
    summres = 0
    ext = False
    while ext == False:
        wr = input('введите числа через пробел или exit - для выхода ').split()
        res = 0
        for el in range(len(wr)):
            if wr[el] == 'exit':
                ext = True
                break
            else:
                res = res + int(wr[el])
        summres = summres + res
        print(f'сумма = {summres}')
sum()