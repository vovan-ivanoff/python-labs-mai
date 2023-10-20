def task_a():
    """задание a: Список квадратов"""
    print([i**2 for i in range(int(input()[3:]), int(input()[3:]) + 1)])
# [i**2 for i in range(a, b + 1)]


if __name__ == '__main__':
    task_a()
