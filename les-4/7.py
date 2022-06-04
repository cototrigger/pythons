from itertools import count
def fact(a):
    factorial = 1

    for x in count(1):
        if x > a:
            break

        factorial = factorial * x
        yield factorial

a = int(input("Укажите целое неотрицательное число: "))
b = 0

for el in fact(a):
    b += 1
    print(f"!{b} = {el}")