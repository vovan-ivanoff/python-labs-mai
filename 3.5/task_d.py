from sys import stdin


def task_d():
    """задание d: Найдётся всё 2.0"""
    lines = list(map(lambda x: x.rstrip('\n'), list(stdin)))
    titles = lines[:-1]
    keyword = lines[-1].lower()
    for title in titles:
        if keyword in title.lower():
            print(title)


if __name__ == '__main__':
    task_d()
