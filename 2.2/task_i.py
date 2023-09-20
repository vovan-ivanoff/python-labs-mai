def task_i():
    """задание i: Первому игроку приготовиться"""
    names = ["", "", ""]
    names[0] = input()
    names[1] = input()
    names[2] = input()
    names.sort()
    print(names[0])


if __name__ == '__main__':
    task_i()
