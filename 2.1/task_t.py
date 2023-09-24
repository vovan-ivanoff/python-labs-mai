"""Задание T"""


def task_t():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    x = (n * (m - k2)) // (k1 - k2)
    print(x, n - x)


if __name__ == '__main__':
    task_t()
