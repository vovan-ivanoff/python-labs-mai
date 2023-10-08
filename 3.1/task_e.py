def task_e():
    """задание e: А роза упала на лапу Азора 4.0"""
    palindr = input()
    if palindr == palindr[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_e()
