def task_c():
    """задание c:Зайка — 8"""
    things = set()
    for _ in range(int(input())):
        things |= set(input().split(" "))
    print("\n".join(things))


if __name__ == '__main__':
    task_c()
