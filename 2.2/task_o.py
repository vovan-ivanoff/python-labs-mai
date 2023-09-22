def task_o():
    """задание o: Властелин Чисел: Возвращение Цезаря"""
    a = input()
    b = input()
    nums = list(a + b)
    nums.sort()
    result = nums[3] + str((int(nums[2]) + int(nums[1])) % 10) + nums[0]
    print(result)


if __name__ == '__main__':
    task_o()
