a = input("Введите выручку:")
b = input("Введите издержки:")
if a > b:
    print('Ура прибыль')
    p = int(a) - int(b)
    r = int(p) / int(a)
    w = int(input('Сколько людей работает?:'))
    i = int(p) / int(w)
    print("Прибыль на одного сотрудника",i)
else:
    print('Эх убыток')