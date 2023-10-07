def task_a():
    """задание a:Азбука"""
    flag = "YES"
    for _ in range(int(input())):
        if input()[0].lower() not in ("а", "б", "в"):
            flag = "NO"
    print(flag)


if __name__ == '__main__':
    task_a()
