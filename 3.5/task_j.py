def task_j():
    """задание j: Хвост"""
    file = input()
    lines = int(input())
    with open(file, "r", encoding="UTF-8") as f:
        print("".join((f.readlines()[-lines:])))


if __name__ == '__main__':
    task_j()
