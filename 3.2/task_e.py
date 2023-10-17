def task_e():
    """задание e: Кашееды — 2"""
    man_lovers = int(input())
    ovs_lovers = int(input())
    lovers = []
    for _ in range(man_lovers + ovs_lovers):
        lovers.append(input())
    # если фамилии повторяются, то мы ее не учитываем
    result = [fam for fam in lovers if lovers.count(fam) == 1]
    print(len(result) if result else "Таких нет")


if __name__ == '__main__':
    task_e()
