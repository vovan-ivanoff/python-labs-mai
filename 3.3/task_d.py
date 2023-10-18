def task_d():
    """задание d: Множество нечетных чисел"""
    numbers = [1, 2, 3, 4]
    print(set([i for i in numbers if i % 2 == 1]))
# set([i for i in numbers if i % 2 == 1])


if __name__ == '__main__':
    task_d()
