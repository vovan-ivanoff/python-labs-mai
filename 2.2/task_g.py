def task_g():
    """задание g: А роза упала на лапу Азора"""
    palindr = input()
    revers = palindr[::-1]
    if palindr == revers:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_g()
