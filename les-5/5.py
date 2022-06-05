a = input("Введите числа через пробел: ")
res = 0

with open("file_5.txt", "w", encoding='utf-8') as obj:
    obj.write(a)

with open("file_5.txt", encoding='utf-8') as obj:
    content = obj.read().split(" ")
    for n in content:
        res = res + int(n)
    print(f"Сумма чисел = {res}")