import json

with open("file_3.json", encoding='utf-8') as read_f:
    data_dict = json.load(read_f)
    print(type(data_dict))
    print("Сотрудники, зарабатывающие менее  20000$ в год:")
    for keys, values in data_dict.items():
        if values < 20000:
            print(keys)
    print(f"Средняя заработная плата = {sum(data_dict.values())/len(data_dict)} $ в год")
