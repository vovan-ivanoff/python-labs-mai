def task_d():
    """задание d: Считалочка 2.0"""
    lower = int(input())
    higher = int(input())
    if lower < higher:
        print(" ".join(map(str, list(range(lower, higher + 1)))))
    else:
        print(" ".join(map(str, list(range(higher, lower + 1))[::-1])))


if __name__ == '__main__':
    task_d()
