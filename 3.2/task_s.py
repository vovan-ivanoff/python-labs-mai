def task_s():
    """задание s: Частная собственность"""
    toys_list = []
    for _ in range(int(input())):
        toys_list.append(list(set(input().split(": ")[1].split(", "))))
    result = []
    for k in toys_list:
        for t in k:
            result.append(t)
    used = []
    for i in reversed(result):
        if result.count(i) > 1 or i in used:
            used.append(i)
            result.remove(i)
    print("\n".join(sorted(result)))


if __name__ == '__main__':
    task_s()
