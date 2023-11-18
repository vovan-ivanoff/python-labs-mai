from itertools import permutations


def task_d():
    "задание d: Словарный комбинатор"
    letters = set(input().split("; "))
    length = int(input())
    result = sorted(list(permutations(letters, length)))
    for c in result:
        print("".join(c))


if __name__ == "__main__":
    task_d()
