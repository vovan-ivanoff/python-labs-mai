def task_g():
    """задание g: Делители"""
    numbers = [15, 36, 49]
    print({num: [i for i in range(1, num + 1) if not num % i]
           for num in numbers})
# {num: [i for i in range(1, num + 1) if not num % i] for num in numbers}


if __name__ == '__main__':
    task_g()
