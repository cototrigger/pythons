a = float (input("Сколько пробежал в первый день: "))
b = float (input("Сколько должен: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = int(a) + int(a) / 10
    day += 1
print(day)