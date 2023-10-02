def task_s():
    """задание s: Числовой квадрат"""
    for i in range(n := int(input())):
        for j in range(n):
            d = str(min(i, j, n - i - 1, n - j - 1) + 1)
            print(d.rjust(len(str((n + 1) // 2)), ' '),
                  end=' ' if j < n - 1 else '\n')


if __name__ == '__main__':
    task_s()
