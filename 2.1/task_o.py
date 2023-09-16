"""Задание O"""


def task_o():
    n = int(input())
    m = int(input())
    t = int(input())
    mins = n * 60 + m
    mins += t
    mins = mins % (24 * 60)
    hours = mins // 60
    minuts = mins % 60
    print(f"{hours:02d}:{minuts:02d}\n")


if __name__ == '__main__':
    task_o()
