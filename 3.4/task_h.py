def task_h():
    """задание h: Меню питания 2.0"""
    kashi = []
    for _ in range(int(input())):
        kashi.append(input())
    for i in range(int(input())):
        print(kashi[i % len(kashi)])


if __name__ == '__main__':
    task_h()
