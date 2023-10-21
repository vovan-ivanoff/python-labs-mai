from itertools import product


def task_i():
    """задание i: Таблица умножения 3.0"""
    power = int(input())
    list_of_lists = [[k for k in range(1, power + 1)] for _ in range(2)]
    for i, j in product(*list_of_lists):
        print(i * j)


if __name__ == '__main__':
    task_i()
