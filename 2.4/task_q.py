def task_q():
    """задание q: А роза упала на лапу Азора 3.0"""
    count = 0
    for _ in range(int(input())):
        num = int(input())
        if str(num) == str(num)[::-1]:
            count += 1
        else:
            continue
    print(count)


if __name__ == '__main__':
    task_q()
