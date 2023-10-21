def task_a():
    """задание a: Автоматизация списка"""
    items = input().split()
    for idx, item in enumerate(items):
        print(f"{idx + 1}. {item}")


if __name__ == '__main__':
    task_a()
