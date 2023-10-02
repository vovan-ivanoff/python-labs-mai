def task_c():
    """задание c: Новогоднее настроение"""
    size = int(input())
    avail_nums = [x for x in range(1, size + 1)]
    counter = 1
    while avail_nums:
        print(" ".join(map(str, avail_nums[:counter])))
        avail_nums = avail_nums[counter:]
        counter += 1


if __name__ == '__main__':
    task_c()
