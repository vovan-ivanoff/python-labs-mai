"""Задание T"""


def task_t():
    n = int(input())
    m = int(input())
    k1 = int(input())
    k2 = int(input())
    cena = m * n
    for i in reversed(range(cena // k1)):
        if (cena - i * k1) % k2 == 0 and i + (cena - i * k1) // k2 == n:
            print(i, (cena - i * k1) // k2)
            break


if __name__ == '__main__':
    task_t()
