def task_k():
    """задание k: Красота спасёт мир"""
    (a, b, c) = list(input())
    if int(a) + int(c) == 2 * int(b):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_k()
