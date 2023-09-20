def task_b():
    """Кто быстрее?"""
    length = 43872
    petya = int(input())
    vasya = int(input())
    time_p = length / petya
    time_v = length / vasya
    if time_p > time_v:
        print("Петя")
    else:
        print("Вася")


if __name__ == '__main__':
    task_b()
