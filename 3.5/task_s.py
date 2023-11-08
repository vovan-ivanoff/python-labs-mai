def task_s():
    """задание s: Это будет наш секрет"""
    offset = int(input())
    out_txt = ""
    with open("public.txt", "r", encoding="UTF-8") as f:
        in_txt = f.read()
    for letter in in_txt:
        if letter.isalpha():
            sh = chr((ord(letter.lower()) - ord('a') + offset) % 26 + ord('a'))
            out_txt += sh if letter.islower() else sh.upper()
        else:
            out_txt += letter
    with open("private.txt", "w", encoding="UTF-8") as f:
        f.write(out_txt)


if __name__ == '__main__':
    task_s()
