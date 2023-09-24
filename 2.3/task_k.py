def task_k():
    """задание k: Цифровая сумма"""
    num = input()
    num_sum = sum(list(map(int, list(num))))
    print(num_sum)


if __name__ == '__main__':
    task_k()
