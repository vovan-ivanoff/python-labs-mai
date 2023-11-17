"""задание i: Циклический генератор"""


def cycle(array):
    i = 0
    while True:
        yield array[i % len(array)]
        i += 1
