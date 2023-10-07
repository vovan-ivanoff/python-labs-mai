def task_c():
    """задание c: Анонс новости"""
    max_len = int(input())
    for _ in range(int(input())):
        if len(header := input()) > max_len:
            print(header[:max_len - 3] + "...")
        else:
            print(header)


if __name__ == '__main__':
    task_c()
