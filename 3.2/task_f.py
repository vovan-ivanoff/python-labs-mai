def task_f():
    """задание f: Кашееды — 3"""
    man_lovers = int(input())
    ovs_lovers = int(input())
    lovers = []
    for _ in range(man_lovers + ovs_lovers):
        lovers.append(input())
    # если фамилии повторяются, то мы ее не учитываем
    result = [fam for fam in lovers if lovers.count(fam) == 1]
    print("\n".join(sorted(result)) if result else "Таких нет")


if __name__ == '__main__':
    task_f()
