from itertools import count, cycle

list_1 = [1, 3, 4, 5, 12, 234]

count = 0
for item in cycle(list_1):
    if count >= len(list_1):
        break
    print(item)
    count += 1