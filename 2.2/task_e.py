def task_e():
    """задание e: Яблоки"""
    n = int(input())
    m = int(input())
    petya = 7 - 3 + 2 + n
    vasya = 6 + 3 + 5 - 2 + m
    if petya > vasya:
        print("Петя")
    else:
        print("Вася")


if __name__ == '__main__':
    task_e()
