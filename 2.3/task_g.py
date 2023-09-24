def task_g():
    """задание g: НОК"""
    a = int(input())
    b = int(input())
    c = a
    d = b
    while a != 0 or b != 0:
        if a > b:
            a -= b
        if a < b:
            b -= a
        if a == b:
            break
    print(c * d // max(a, b))


if __name__ == '__main__':
    task_g()
