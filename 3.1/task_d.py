def task_d():
    """задание d: Очистка данных"""
    while (data := input()) != "":
        if data.startswith("##"):
            data = data[2:]
        if data.endswith("@@@"):
            pass
        else:
            print(data)


if __name__ == '__main__':
    task_d()
