from sys import stdin


def task_a():
    """задание a: A+B+..."""
    nums = []
    for line in stdin:
        nums += [*map(int, line.split())]
    print(sum(nums))


if __name__ == '__main__':
    task_a()
