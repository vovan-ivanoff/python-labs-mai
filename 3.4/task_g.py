from itertools import combinations as c


def task_g():
    """задание g: Игровая сетка"""
    names = []
    for _ in range(int(input())):
        names.append(input())
    for name1, name2 in c(names, 2):
        print(name1, name2, sep=" - ")


if __name__ == '__main__':
    task_g()
