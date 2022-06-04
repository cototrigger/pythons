list_l = [1,2,3,4,5,6,7,8,9,0,2,4,6,7,9,0,4]

list_1 = [el for el in list_l if list_l.count(el) == 1]

print(list_1)