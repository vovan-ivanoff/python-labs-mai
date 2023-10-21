def task_b():
    """задание b: Сборы на прогулку"""
    list_1 = input().split(", ")
    list_2 = input().split(", ")
    if len(list_1) > len(list_2):
        list_1 = list_1[:len(list_2)]
    elif len(list_1) < len(list_2):
        list_2 = list_2[:len(list_1)]
    for idx, name in enumerate(list_1):
        print(f"{name} - {list_2[idx]}")


if __name__ == '__main__':
    task_b()
