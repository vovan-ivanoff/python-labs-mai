"""Задание J"""


def task_j():
    name = input()
    nomer = input()
    g, k, n = nomer[0], nomer[1], nomer[2]
    print(f"Группа №{g}.\n{n}. {name}.\nШкафчик: {nomer}.\nКроватка: {k}.")


if __name__ == '__main__':
    task_j()
