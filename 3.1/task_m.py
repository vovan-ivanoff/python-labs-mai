def task_m():
    """задание m: Массовое возведение в степень"""
    numbers = []
    for _ in range(int(input())):
        numbers.append(int(input()))
    power = int(input())
    for num in numbers:
        print(num ** power)


if __name__ == '__main__':
    task_m()
