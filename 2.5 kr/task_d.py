def task_d():
    "задание d: Особый максимум"
    less_than_prev = []
    prev = 0
    for k in range(int(input())):
        if (n := int(input())) < prev and k != 0:
            less_than_prev.append(n)
        prev = n
    if len(less_than_prev) > 0:
        print(max(less_than_prev))


if __name__ == "__main__":
    task_d()
