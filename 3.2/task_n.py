def task_n():
    """задание n: Это будет шеддеввввр!"""
    avail_products = set()
    recepies = {}
    for _ in range(int(input())):
        avail_products.add(input())
    for _ in range(int(input())):
        recepies[name := input()] = set()
        for _ in range(int(input())):
            recepies[name].add(input())
    flag = False
    for recepie in sorted(recepies.keys()):
        if recepies[recepie] <= avail_products:
            print(recepie)
            flag = True
    if not flag:
        print("Готовить нечего")


if __name__ == '__main__':
    task_n()
