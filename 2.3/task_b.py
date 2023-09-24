def task_b():
    """задание b: Зайка — 3"""
    counter = 0
    while (land := input()) != "Приехали!":
        if "зайка" in land:
            counter += 1
    print(counter)


if __name__ == '__main__':
    task_b()
