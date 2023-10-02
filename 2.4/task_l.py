def task_l():
    """задание l: Числовой прямоугольник"""
    height = int(input())
    width = int(input())
    avail_nums = list(range(1, width * height + 1))
    max_len = len(str(width * height))
    for x in range(height):
        result = ""
        for y in range(width):
            result += str(avail_nums[y + x * width]).rjust(max_len + 1)
        print(result[1:])


if __name__ == '__main__':
    task_l()
