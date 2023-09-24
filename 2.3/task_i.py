def task_i():
    """задание i: Факториал"""
    chislo = int(input())
    result = 1
    for i in range(1, chislo + 1):
        result *= i
    print(result)


if __name__ == '__main__':
    task_i()
