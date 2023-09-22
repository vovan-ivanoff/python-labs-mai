def task_q():
    """задание q: Корень зла"""
    a = float(input())
    b = float(input())
    c = float(input())
    if a == b == 0:
        print("Infinite solutions")
        return
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No solution")
        return
    if discriminant == 0:
        x = -1 * b / (2 * a)
        print(f"{x:.02f}")
    elif discriminant > 0:
        x1 = (-1 * b + discriminant ** 0.5) / (2 * a)
        x2 = (-1 * b - discriminant ** 0.5) / (2 * a)
        print(f"{min(x1, x2):.02f} {max(x1, x2):.02f}")


if __name__ == '__main__':
    task_q()
