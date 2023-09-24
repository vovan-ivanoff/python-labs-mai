def task_m():
    """задание m: Первому игроку приготовиться 2.0"""
    num = int(input())
    array = []
    for _ in range(num):
        array.append(input())
    print(min(array))


if __name__ == '__main__':
    task_m()
