def task_b():
    """задание b: Не таблица умножения"""
    power = int(input()) + 1
    for i in range(1, power):
        for k in range(1, power):
            print(f"{k} * {i} = {i * k}")


if __name__ == '__main__':
    task_b()
