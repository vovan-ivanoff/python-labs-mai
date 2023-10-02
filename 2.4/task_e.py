def task_e():
    """задание e: Зайка — 5"""
    number_areas = int(input())
    counter = 0
    for _ in range(number_areas):
        flag = True
        while (piece := input()) != "ВСЁ":
            if flag and piece == "зайка":
                counter += 1
                flag = False
    print(counter)


if __name__ == '__main__':
    task_e()
