def task_h():
    """задание h: Кашееды — 4"""
    kash_dict = {}
    for _ in range(int(input())):
        name, *kasha = input().split(" ")
        kash_dict[name] = kasha
    needed = input()
    flag = False
    for name in sorted(kash_dict.keys()):
        if needed in kash_dict[name]:
            print(name)
            flag = True
    if not flag:
        print("Таких нет")


if __name__ == '__main__':
    task_h()
