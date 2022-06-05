import json

profit = {}
f_profit = {}
data = [f_profit, profit]
sum_m = 0
count_f = 0

with open("file_7.txt", encoding='cp1251') as f:
    for line in f:
        name, form, salary, cost = line.split()
        margin = float(salary) - float(cost)
        if margin > 0:
            count_f = count_f + 1
            sum_m = sum_m + margin
            f_profit[name] = margin
if count_f > 0:
    profit["Profit"] = sum_m / count_f

with open("file_7.json", "w", encoding='cp1251') as write_f:
    json.dump(data, write_f)
print(f"{f_profit} {profit}")
