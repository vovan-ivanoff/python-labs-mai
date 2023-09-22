def task_j():
    """задание j: шифрование"""
    chislo = input()
    c = int(chislo[0])
    b = int(chislo[1])
    a = int(chislo[2])
    res = []
    res.append(a + b)
    res.append(b + c)
    res.sort()
    print(str(res[1])+str(res[0]))


if __name__ == '__main__':
    task_j()
