def task_k():
    """задание k: Простая задача 3.0"""
    counter = 0
    for _ in range(int(input())):
        num = int(input())
        if num == 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            counter += 1
    print(counter)


if __name__ == '__main__':
    task_k()
