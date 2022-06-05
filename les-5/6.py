obj = {}
with open("file_6.txt", encoding='utf-8') as f:
    for line in f:
        clear_line = line.replace("(л)", "").replace("(пр)", "").replace("(лаб)", "").replace(".", "")
        subject, lecture, practice, lab = clear_line.split()
        lect_int = 0
        practice_int = 0
        lab_int = 0
        if lecture != "-":
            lect_int = int(lecture)
        if practice != "-":
            practice_int = int(practice)
        if lab != "-":
            lab_int = int(lab)
        obj[subject] = lect_int + practice_int + lab_int
    print(f"{obj}")
    f.close()
