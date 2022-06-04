list_l = [100, 34, 11, 4, 8, 7, 8, 2354, 63]

list_1 = [list_l[el] for el in range(
    1, len(list_l)) if list_l[el] > list_l[el - 1]]

print(list_1)