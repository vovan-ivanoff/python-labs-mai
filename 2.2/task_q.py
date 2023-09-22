def task_q():
    """задание q: Корень зла"""
    a = float(input())
    b = float(input())
    c = float(input())
    if a == b == 0:
        print("Infinite solutions")
        return
    discriminant = b ** 2 - 4*a*c
    if discriminant < 0:
        print("No solution")
        return
    if discriminant == 0:
        x = -b / (2*a)
        print(f"{x:.02f}")
    elif discriminant > 0:
        x1 = -b + discriminant ** 0.5
        x2 = -b - discriminant ** 0.5
        print(f"{x1:.02f} {x2:.02f}")


if __name__ == '__main__':
    task_q()
