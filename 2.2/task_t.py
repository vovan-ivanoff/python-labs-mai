def task_t():
    """задание t: Зайка — 2"""
    str_a = input()
    str_b = input()
    str_c = input()
    massiv = sorted([str_a, str_b, str_c])
    if "зайка" in massiv[0]:
        print(massiv[0], len(massiv[0]))
    elif "зайка" in massiv[1]:
        print(massiv[1], len(massiv[1]))
    elif "зайка" in massiv[2]:
        print(massiv[2], len(massiv[2]))


if __name__ == '__main__':
    task_t()
