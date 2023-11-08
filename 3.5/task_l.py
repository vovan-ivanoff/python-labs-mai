def task_l():
    """задание l: Разделяй и властвуй"""
    infile = input()
    even = input()
    odd = input()
    eq = input()
    nums = []
    with open(infile, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            nums += [line.split()]
    with open(even, "w", encoding="UTF-8") as f:
        res = []
        for line in nums:
            res.append(" ".join([x for x in line
                                 if sum([x.count(str(i))
                                         for i in range(0, 10, 2)])
                                 > sum([x.count(str(i))
                                        for i in range(1, 10, 2)])]))
        f.write("\n".join(res) + "\n")
    with open(odd, "w", encoding="UTF-8") as f:
        res = []
        for line in nums:
            res.append(" ".join([x for x in line
                                 if sum([x.count(str(i))
                                         for i in range(0, 10, 2)])
                                 < sum([x.count(str(i))
                                        for i in range(1, 10, 2)])]))
        f.write("\n".join(res) + "\n")
    with open(eq, "w", encoding="UTF-8") as f:
        res = []
        for line in nums:
            res.append(" ".join([x for x in line
                                 if sum([x.count(str(i))
                                         for i in range(0, 10, 2)])
                                 == sum([x.count(str(i))
                                         for i in range(1, 10, 2)])]))
        f.write("\n".join(res) + "\n")


if __name__ == '__main__':
    task_l()
