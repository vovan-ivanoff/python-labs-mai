def task_r():
    """задание r: Карта сокровищ"""
    d = {}
    for _ in range(int(input())):
        x = input().split()
        if not (z := f'{x[0][:-1]}-{x[1][:-1]}') in d:
            d[z] = 1
        else:
            d[z] += 1
    print(max(d.values()))


if __name__ == '__main__':
    task_r()
