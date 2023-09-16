"""Задание L"""


def task_l():
    a = input()
    b = input()
    a = "00" + a
    b = "00" + b
    res = (int(a[-1]) + int(b[-1])) % 10 + \
        (int(a[-2]) + int(b[-2])) % 10 * 10 + \
        (int(a[-3]) + int(b[-3])) % 10 * 100
    print(res)


if __name__ == '__main__':
    task_l()
