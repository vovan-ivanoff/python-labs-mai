def task_p():
    """задание p: А роза упала на лапу Азора 2.0"""
    num = int(input())
    if str(num) == str(num)[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_p()
