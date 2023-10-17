def task_m():
    """задание m: Дайте чего-ниудь новенького"""
    avail_bluda = set()
    prev_bluda = set()
    for _ in range(int(input())):
        avail_bluda.add(input())
    for _ in range(int(input())):
        for _ in range(int(input())):
            prev_bluda.add(input())
    if len(avail_bluda - prev_bluda) == 0:
        print("Готовить нечего")
        return
    print("\n".join(sorted(list(avail_bluda - prev_bluda))))


if __name__ == '__main__':
    task_m()
