str = input("Напишите слова через пробел: ")
a = str.split(' ')
for b, c in enumerate(a, 1):
    if len(c) > 10:
        c = c[0:10]
    print(f"{b}. - {c}")