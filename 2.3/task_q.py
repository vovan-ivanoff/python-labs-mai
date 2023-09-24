def task_q():
    """задание q: Чётная чистота"""
    num = input()
    for char in range(0, 10, 2):
        num = num.replace(str(char), "")
    print(num)


if __name__ == '__main__':
    task_q()
