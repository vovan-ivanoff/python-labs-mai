def task_f():
    """задание f: НОД 2.0"""
    numbers = sorted([int(input()) for _ in range(int(input()))])
    prev_nod = numbers[-1]
    for num in numbers:
        while prev_nod != num:
            if prev_nod > num:
                prev_nod -= num
            if prev_nod < num:
                num -= prev_nod
    print(prev_nod)


if __name__ == '__main__':
    task_f()
