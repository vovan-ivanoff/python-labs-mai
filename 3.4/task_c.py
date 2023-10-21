from itertools import count as c


def task_c():
    """задание c: Рациональная считалочка"""
    begin, end, step = map(float, input().split())
    for num in c(begin, step):
        if num > end:
            break
        print(f"{num:.2f}")


if __name__ == '__main__':
    task_c()
