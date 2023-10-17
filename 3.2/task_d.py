def task_d():
    """задание d:Кашееды"""
    man_lovers = int(input())
    ovs_lovers = int(input())
    manaya = set()
    ovsana = set()
    for _ in range(man_lovers):
        manaya.add(input())
    for _ in range(ovs_lovers):
        ovsana.add(input())
    both = len(manaya & ovsana)
    print("Таких нет" if both == 0 else both)


if __name__ == '__main__':
    task_d()
