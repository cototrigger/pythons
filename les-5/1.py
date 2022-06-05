a = open("file_1.txt", 'w', encoding='utf-8')
lines = []
while True:
    line = input("Введите данные или нажмите Enter для завершения: ")
    if line != '':
        lines.append(line + "\n")
    else:
        break
a.writelines(lines)

with open("file_1.txt", "r", encoding='utf-8') as a:
    for line in a:
        print(line)
