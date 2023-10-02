def task_r():
    """задание r: Новогоднее настроение 2.0"""
    size = int(input())
    avail_nums = [x for x in range(1, size + 1)]
    counter = 1
    result = []
    while avail_nums:
        result.append(avail_nums[:counter])
        avail_nums = avail_nums[counter:]
        counter += 1
    max_len = len(" ".join(map(str, result[-1])))
    for layer in result:
        print(f"{' '.join(map(str, layer)):^{max_len}}")


if __name__ == '__main__':
    task_r()
