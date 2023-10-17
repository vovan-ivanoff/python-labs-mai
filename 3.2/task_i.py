def task_i():
    """задание i Зайка — 9"""
    things = {}
    while (land := input()) != "":
        seen = land.split(" ")
        for thing in seen:
            if thing not in things:
                things[thing] = 0
            things[thing] += 1
    for th in things.items():
        print(*th)


if __name__ == '__main__':
    task_i()
