from itertools import accumulate as acc


def task_d():
    """задание d: Словарная ёлка"""
    things = [s + " " for s in input().split()]
    for thing in acc(things):
        print(thing.rstrip())


if __name__ == '__main__':
    task_d()
