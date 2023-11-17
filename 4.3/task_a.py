"""Рекурсивный сумматор"""


def recursive_sum(*args):
    rsum = 0
    if len(args) == 0:
        return rsum
    return args[0] + recursive_sum(*args[1::])
