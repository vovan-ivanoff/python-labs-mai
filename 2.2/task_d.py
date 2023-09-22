def task_d():
    """задание d: Список Победителей"""
    members = {int(input()): "Петя", int(input()): "Вася",
               int(input()): "Толя"}
    lis = list(members.keys())
    lis.sort()
    print(f"1. {members[lis[2]]}")
    print(f"2. {members[lis[1]]}")
    print(f"3. {members[lis[0]]}")


if __name__ == '__main__':
    task_d()
