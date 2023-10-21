def task_e():
    """задание e: Список покупок"""
    a, b, c = [input().split(", ") for _ in range(3)]
    a += (b + c)
    for idx, item in enumerate(sorted(a)):
        print(f"{idx + 1}. {item}")


if __name__ == '__main__':
    task_e()
