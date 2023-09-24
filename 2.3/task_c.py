def task_c():
    """задание c: Считалочка"""
    lower = int(input())
    higher = int(input())
    print(" ".join(map(str, list(range(lower, higher + 1)))))


if __name__ == '__main__':
    task_c()
