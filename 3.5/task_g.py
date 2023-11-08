def task_g():
    """задание g: Файловая статистика"""
    filename = input()
    nums = []
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            nums += [*map(int, line.split())]
    print(len(nums))
    print(len([x for x in nums if x > 0]))
    print(min(nums))
    print(max(nums))
    print(sum(nums))
    print(f"{(sum(nums) / len(nums)):.2f}")


if __name__ == '__main__':
    task_g()
