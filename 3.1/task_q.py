def task_q():
    """задание q: А роза упала на лапу Азора 5.0"""
    palindr = input().lower().replace(" ", "")
    if palindr == palindr[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    task_q()
