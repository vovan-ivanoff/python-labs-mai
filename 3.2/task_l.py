def task_l():
    """задание l: Однофамильцы - 2"""
    muzhiki = []
    for _ in range(int(input())):
        muzhiki.append(input())
    for mzh in set(muzhiki):
        if muzhiki.count(mzh) == 1:
            muzhiki.remove(mzh)
    if not muzhiki:
        print("Однофамильцев нет")
        return
    for muzhik in sorted(set(muzhiki)):
        print(f"{muzhik} - {muzhiki.count(muzhik)}")


if __name__ == '__main__':
    task_l()
