"""Задание Q"""


def task_q():
    a = int(input())
    b = input()
    b = b[::-1]
    res = 0
    for i in range(len(b)):
        res += int(b[i]) * (2 ** i)
    print(a + res)


if __name__ == '__main__':
    task_q()
