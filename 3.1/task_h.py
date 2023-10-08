def task_h():
    """задание h: Зайка — 7"""
    for _ in range(int(input())):
        if (pos := input().find("зайка")) != -1:
            print(pos + 1)
        else:
            print("Заек нет =(")


if __name__ == '__main__':
    task_h()
