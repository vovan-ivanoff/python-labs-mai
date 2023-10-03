def task_t():
    """задание t:математическая выгода"""
    n = int(input())
    best_degree = 0
    best_sum = -1
    for d in range(2, 11):
        num_another = ""
        copy_n = n
        while copy_n != 0:
            num_another += str(copy_n % d)
            copy_n //= d
        cur_sum = sum(list(map(int, list(num_another))))
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_degree = d
    print(best_degree)


if __name__ == '__main__':
    task_t()
