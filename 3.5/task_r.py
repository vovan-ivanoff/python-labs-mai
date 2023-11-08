import os


def task_r():
    """задание r: Сколько вешать в байтах?"""
    size = os.stat(input()).st_size
    if size > 2**30 - 1:
        s = int(size / (2 ** 30)) + 1
        unit = "ГБ"
    elif size > 2**20 - 1:
        s = int(size / (2 ** 20)) + 1
        unit = "МБ"
    elif size > 2**10 - 1:
        s = int(size / (2 ** 10)) + 1
        unit = "КБ"
    else:
        s = size
        unit = "Б"
    print(str(s) + unit)


if __name__ == '__main__':
    task_r()
