def task_a():
    """задание a: Таблица умножения"""
    power = int(input()) + 1
    for i in range(1, power):
        result = str(i)
        for k in range(2, power):
            result += (" " + str(i * k))
        print(result)


if __name__ == '__main__':
    task_a()
