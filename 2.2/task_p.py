def task_p():
    """задание p: Легенды велогонок возвращаются: кто быстрее?"""
    members = {int(input()): "Петя", int(input()): "Вася",
               int(input()): "Толя"}
    lis = list(members.keys())
    lis.sort()
    print(f"{members[lis[2]]:^24}")
    print(f"  {members[lis[1]]:<22}")
    print(f"{members[lis[0]]:>22}")
    print("   II      I      III   ")


if __name__ == '__main__':
    task_p()
