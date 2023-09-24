def task_o():
    """задание o: Зайка - 4"""
    a = int(input())
    counter = 0
    for _ in range(a):
        if 'зайка' in input():
            counter += 1
    print(counter)


if __name__ == '__main__':
    task_o()
