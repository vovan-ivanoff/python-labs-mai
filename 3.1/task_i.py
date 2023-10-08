def task_i():
    """задание i: Без комментариев"""
    while (data := input()) != "":
        data = data.split("#")[0].rstrip()
        if data:
            print(data)


if __name__ == '__main__':
    task_i()
