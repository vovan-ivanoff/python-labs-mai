def task_e():
    """задание e: Множество всех полных квадратов"""
    numbers = [1, 2, 4, 16, 25]
    print(set([i for i in numbers if i ** 0.5 % 1 == 0]))
# set([i for i in numbers if i ** 0.5 % 1 == 0])


if __name__ == '__main__':
    task_e()
