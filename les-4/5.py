from functools import reduce

list_1 = [x for x in range(100, 1001, 2)]

res = reduce(lambda a, b: a * b, list_1)

print(list_1)
print(f"Результат: {res}")
