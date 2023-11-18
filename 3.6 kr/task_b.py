def task_b():
    "задание b: Словарная опись"
    in_words = []
    out_dict = {}
    while (data := input()) != "":
        in_words += data.split()
    for word in in_words:
        middle = int(len(word) / 2)
        if len(word) % 2 == 0:
            middle_letter = word.lower()[middle - 1:middle]
        else:
            middle_letter = word.lower()[middle:middle + 1]
        if middle_letter not in out_dict:
            out_dict[middle_letter] = [word.upper()]
        else:
            out_dict[middle_letter].append(word.upper())
    for key in out_dict:
        print(f'{key} "{". ".join(sorted(list(set(out_dict[key]))))}"')


if __name__ == "__main__":
    task_b()
