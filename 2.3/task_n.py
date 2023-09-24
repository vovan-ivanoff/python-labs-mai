def task_n():
    """задание n: Простая задача"""
    num = int(input())
    if num == 1:
        print("NO")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    task_n()
