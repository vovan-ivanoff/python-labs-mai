def task_b():
    """задание b: Таблица умножения 2.0"""
    n = int(input())
    print([[num * k for num in range(1, n + 1)] for k in range(1, n + 1)])
# [[num * k for num in range(1, n + 1)] for k in range(1, n + 1)]


if __name__ == '__main__':
    task_b()
