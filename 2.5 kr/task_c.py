def task_c():
    "задание c: Счёт с пропусками"
    m = int(input())
    n = int(input())
    print(", ".join(map(str, list(range(n, m + 1, ((n - m) % 10))))))


if __name__ == "__main__":
    task_c()
