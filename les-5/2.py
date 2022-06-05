lines = 0
words = 1

with open("file_2.txt", "r", encoding='utf-8') as a:
    for line in a:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                words += 1
        lines += 1
        print(f"Количество слов в строке №{lines} = {words} \n")
        words = 1
    print(f"В файле {lines} строк(и)")