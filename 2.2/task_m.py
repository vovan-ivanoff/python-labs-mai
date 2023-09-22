def task_m():
    """задание m: Властелин Чисел: Братство общей цифры"""
    num_a = input()
    num_b = input()
    num_c = input()
    if num_a[0] in num_b and num_c:
        print(num_a[0])
    elif num_a[1] in num_b and num_c:
        print(num_a[1])
    elif num_b[0] in num_a and num_c:
        print(num_b[0])
    elif num_b[1] in num_a and num_c:
        print(num_b[0])
    elif num_c[0] in num_b and num_a:
        print(num_c[0])
    elif num_c[1] in num_b and num_a:
        print(num_c[0])


if __name__ == '__main__':
    task_m()
