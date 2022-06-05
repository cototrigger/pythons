list_l = [100, 34, 11, 4, 8, 7, 8, 2354, 63]

list_1 = []
for el in range(1, len(list_l)):
    if list_l[el] > list_l[el - 1]:
        list_1.append(list_l[el])

print(list_1)