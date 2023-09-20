def task_c():
    """задание c: Кто быстрее на этот раз?"""
    length = 43872
    petya = int(input())
    vasya = int(input())
    tolya = int(input())
    time_p = length / petya
    time_v = length / vasya
    time_t = length / tolya
    time = min(time_p, time_v, time_t)
    if time == time_v:
        print("Вася")
    elif time == time_p:
        print("Петя")
    elif time == time_t:
        print("Толя")


if __name__ == '__main__':
    task_c()
