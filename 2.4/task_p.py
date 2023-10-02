def task_p():
    """задание p: Редизайн таблицы умножения"""
    a = int(input())
    b = int(input())
    for i in range(2, (a + 1) * 2 - 1):
        result = ""
        if i % 2 != 0:
            print("-" * (a * b + (a - 1)))
        else:
            for k in range(2, (a + 1) * 2 - 1):
                if k % 2 != 0:
                    result += "|"
                else:
                    result += f"{(i // 2) * (k // 2):^{b}}"
            print(result)


if __name__ == '__main__':
    task_p()
