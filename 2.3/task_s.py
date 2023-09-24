def task_s():
    """задание s: Игра в «Угадайку»"""
    begin, end = 1, 1001
    print((begin + end) // 2)
    while (x := input()) != 'Угадал!':
        if x == 'Меньше':
            end = (begin + end) // 2
            print(((begin + end) // 2))
        elif x == 'Больше':
            begin = (begin + end) // 2
            print(((begin + end) // 2))


if __name__ == '__main__':
    task_s()
