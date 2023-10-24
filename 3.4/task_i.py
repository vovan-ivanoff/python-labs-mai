from itertools import product


def task_i():
    """задание i: Таблица умножения 3.0"""
    power = int(input())
    list_nums = list(range(1, power + 1))
    for i in range(1, power + 1):
        print(" ".join(map(lambda x: str(x[0] * x[1]),
              list(product(list_nums, [i])))))


if __name__ == '__main__':
    task_i()
