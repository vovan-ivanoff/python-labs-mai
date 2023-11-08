from sys import stdin


def task_c():
    """задание c: Без комментариев 2.0"""
    for data in stdin:
        data = data.split("#")[0].rstrip()
        if data:
            print(data)


if __name__ == '__main__':
    task_c()
