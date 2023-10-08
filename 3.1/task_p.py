def task_p():
    """задание p: Анонс новости 2.0"""
    max_len = int(input())
    header_lines = []
    for _ in range(int(input())):
        header_lines.append(input())
    for i in header_lines:
        if max_len > 3:
            print(i[:max_len - 3] + "..." if len(i) >= max_len - 3
                  else (i + "..." if max_len == 4 else i))
        max_len -= len(i)


if __name__ == '__main__':
    task_p()
