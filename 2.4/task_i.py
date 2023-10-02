def task_i():
    """задание i: Большое число"""
    result = ""
    for _ in range(int(input())):
        max_digit = max(map(int, list(input())))
        result += str(max_digit)
    print(result)


if __name__ == '__main__':
    task_i()
