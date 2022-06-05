a = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("file_4.txt", encoding='utf-8') as obj:
    for line in obj:
        for key in a.keys():
            line = line.replace(key, a[key])
        print(line)
        with open("file_4.1.txt", "a") as per:
            per.write(f"\n {line}")