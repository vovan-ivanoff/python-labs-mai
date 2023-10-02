def task_o():
    """задание o: Числовая змейка 2.0"""
    height = int(input())
    width = int(input())
    avail_nums = list(range(1, width * height + 1))
    max_len = len(str(width * height))
    for x in range(height):
        result = ""
        for y in range(width):
            if y % 2 == 0:
                result += str(avail_nums[x + y * height]).rjust(max_len + 1)
            else:
                result += str(avail_nums[(y + 1) * height
                                         - x - 1]).rjust(max_len + 1)
        print(result[1:])


if __name__ == '__main__':
    task_o()
