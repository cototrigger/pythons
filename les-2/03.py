number = int(input("Введите номер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {
         1: 'зимы',
         2: 'зимы',
         3: 'весны',
         4: 'весны',
         5: 'весны',
         6: 'лета',
         7: 'лета',
         8: 'лета',
         9: 'осени',
         10: 'осени',
         11: 'осени',
         12: 'зимы'
 }
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Это месяц {month_list[i]}")
            break
    print(f"Это месяц {month_dict[number]}")
else:
    print("error")