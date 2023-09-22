def task_r():
    """задание r: Территроия зла"""
    a = int(input())
    b = int(input())
    c = int(input())
    massiv = [a, b, c]
    massiv.sort()
    if massiv[2] ** 2 == massiv[1] ** 2 + massiv[0] ** 2:
        print("100%")
    elif massiv[2] ** 2 > massiv[1] ** 2 + massiv[0] ** 2:
        print("велика")
    elif massiv[2] ** 2 < massiv[1] ** 2 + massiv[0] ** 2:
        print("крайне мала")


if __name__ == '__main__':
    task_r()
