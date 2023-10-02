def task_h():
    """задание h: Максимальная сумма"""
    max_sum = 0
    winner = ""
    for _ in range(int(input())):
        name = input()
        cur_sum = sum(map(int, input()))
        if cur_sum >= max_sum:
            max_sum = cur_sum
            winner = name
    print(winner)


if __name__ == '__main__':
    task_h()
