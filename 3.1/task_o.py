def task_o():
    """задание o: НОД 3.0"""
    numbers = sorted(list(map(int, input().split(" "))))
    prev_nod = numbers[-1]
    for num in numbers:
        while prev_nod != num:
            if prev_nod > num:
                prev_nod -= num
            if prev_nod < num:
                num -= prev_nod
    print(prev_nod)


if __name__ == '__main__':
    task_o()
