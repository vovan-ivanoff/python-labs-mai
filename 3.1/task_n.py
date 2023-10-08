def task_n():
    """задание n:Массовое возведение в степень 2.0"""
    numbers = list(map(int, input().split(" ")))
    power = int(input())
    print(" ".join([str(x ** power) for x in numbers]))


if __name__ == '__main__':
    task_n()
