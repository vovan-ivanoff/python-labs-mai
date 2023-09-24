def task_j():
    """задание j: Маршрут построен"""
    x = 0
    y = 0
    while (direction := input()) != "СТОП":
        if direction == "СЕВЕР":
            y += int(input())
        if direction == "ЮГ":
            y -= int(input())
        if direction == "ЗАПАД":
            x -= int(input())
        if direction == "ВОСТОК":
            x += int(input())
    print(y)
    print(x)


if __name__ == '__main__':
    task_j()
