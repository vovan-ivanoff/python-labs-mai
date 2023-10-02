def task_d():
    """задание d: Суммарная сумма"""
    number = int(input())
    result = 0
    for _ in range(number):
        result += sum(map(int, input()))
    print(result)


if __name__ == '__main__':
    task_d()
