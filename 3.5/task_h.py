def task_h():
    """задание h: Файловая разница"""
    firstfile = input()
    secondfile = input()
    outfile = input()
    with open(firstfile, "r", encoding="UTF-8") as f:
        slova = set(f.read().replace("\n", " ").split())
    with open(secondfile, "r", encoding="UTF-8") as f:
        slova ^= set(f.read().replace("\n", " ").split())
    with open(outfile, "w", encoding="UTF-8") as f:
        f.writelines(map(lambda x: x + "\n", sorted(slova)))


if __name__ == '__main__':
    task_h()
