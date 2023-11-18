def task_c():
    "задание c: Перераспределение по размеру"
    nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
    print([i for i in sorted(nums, key=lambda x: not
                             (x > (max(nums) + min(nums)) / 2))])


if __name__ == "__main__":
    task_c()
