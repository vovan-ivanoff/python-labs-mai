def task_a():
    "задание a: Форматированная математика"
    a = int(input())
    b = int(input())
    c = int(input())
    print(f"{a} ^ ({b} mod {c}) = {a ** (b % c)}")


if __name__ == "__main__":
    task_a()
