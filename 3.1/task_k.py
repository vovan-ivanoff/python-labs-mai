def task_k():
    """задание k:Найдётся всё"""
    titles = []
    for _ in range(int(input())):
        titles.append(input())
    keyword = input().lower()
    for title in titles:
        if keyword in title.lower():
            print(title)


if __name__ == '__main__':
    task_k()
