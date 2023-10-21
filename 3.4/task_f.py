from itertools import product


def task_f():
    """задание f:Колода карт"""
    masti = ["пик", "треф", "бубен", "червей"]
    cards = list(range(2, 11)) + ["валет", "дама", "король", "туз"]
    masti.remove(input())
    for value, mast in product(cards, masti):
        print(value, mast)


if __name__ == '__main__':
    task_f()
