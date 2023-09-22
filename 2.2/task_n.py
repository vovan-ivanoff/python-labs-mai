def task_n():
    """задание n: Властелин Чисел: Две Башни"""
    chislo = list(input())
    chislo.sort()
    maximus = chislo[2] + chislo[1]
    if chislo[0] == '0':
        minimus = chislo[1] + chislo[0]
    else:
        minimus = chislo[0] + chislo[1]
    print(f"{minimus} {maximus}")


if __name__ == '__main__':
    task_n()
