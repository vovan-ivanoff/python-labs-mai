from itertools import combinations_with_replacement, permutations


def task_j():
    """задание j: Мы делили апельсин 2.0"""
    num = int(input())
    k = list(combinations_with_replacement(list(range(1, num - 1)), 3))
    k = list(map(lambda x: permutations(x, 3), k))
    for i in k:
        if sum(i) == num:
            print(*i)


if __name__ == '__main__':
    task_j()
