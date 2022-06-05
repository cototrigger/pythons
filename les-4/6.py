from itertools import count, cycle

list_1 = []

a = int(input("Укажите первое число: "))
b = int(input("Укажите последнее число: "))

for x in count(a):
    if x > b:
        break
print(x)

list_1.append(x)