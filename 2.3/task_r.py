def task_r():
    """задание r: Простая задача 2.0"""
    num = int(input())
    divisors = []
    while num > 1:
        for i in range(2, num + 1):
            if num % i == 0:
                divisors.append(i)
                num //= i
                break
    print(" * ".join(map(str, divisors)))


if __name__ == '__main__':
    task_r()
