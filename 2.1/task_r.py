"""Задание R"""


def task_r():
    b = input()
    b = b[::-1]
    a = int(input())
    res = 0
    for i in range(len(b)):
        res += int(b[i]) * (2 ** i)
    print(a - res)


if __name__ == '__main__':
    task_r()
