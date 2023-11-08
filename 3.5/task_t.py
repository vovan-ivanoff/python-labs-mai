def task_t():
    """задание t: Файловая сумма"""
    result = 0
    with open("numbers.num", "rb") as f:
        while data := f.read(2):
            if len(data) > 1:
                result += int.from_bytes(data)
    print(result % 2**16)


if __name__ == '__main__':
    task_t()
