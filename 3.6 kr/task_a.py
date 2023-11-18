def task_a():
    "задание a: Шинковка строк"
    for _ in range(int(input())):
        data = input().split("^")
        begin = int(data[1])
        end = int(data[2])
        step = len(data[0]) % 4
        print(str(data[0])[begin:end:step])


if __name__ == "__main__":
    task_a()
