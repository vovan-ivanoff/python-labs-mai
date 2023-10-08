def task_f():
    """задание f: Зайка — 6"""
    counter = 0
    for _ in range(int(input())):
        land = input()
        counter += land.count("зайка")
    print(counter)


if __name__ == '__main__':
    task_f()
