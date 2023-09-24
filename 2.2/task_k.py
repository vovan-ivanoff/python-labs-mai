def task_k():
    """задание k: Красота спасёт мир"""
    chislo = sorted(list(input()))
    if int(chislo[0]) + int(chislo[2]) == 2 * int(chislo[1]):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_k()
