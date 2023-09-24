def task_f():
    """задание f: НОД"""
    a = int(input())
    b = int(input())
    while a != 0 or b != 0:
        if a > b:
            a -= b
        if a < b:
            b -= a
        if a == b:
            break
    print(max(a, b))


if __name__ == '__main__':
    task_f()
