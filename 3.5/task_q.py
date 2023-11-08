def task_q():
    """задание q: Прятки"""
    out_str = ""
    with open("secret.txt", "r", encoding="UTF-8") as f:
        in_str = f.read()
    for sym in in_str:
        out_str += chr(ord(sym) % 128)
    print(out_str)


if __name__ == '__main__':
    task_q()
