def task_k():
    """задание k: Однофамильцы"""
    muzhiki = []
    muzhiki_uniq = set()
    for _ in range(int(input())):
        muzh = input()
        muzhiki.append(muzh)
        muzhiki_uniq.add(muzh)
    for mzh in muzhiki_uniq:
        if muzhiki.count(mzh) == 1:
            muzhiki.remove(mzh)
    print(len(muzhiki))


if __name__ == '__main__':
    task_k()
