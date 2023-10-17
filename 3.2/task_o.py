def task_o():
    """задание o: двоичная статистика!"""
    numbers = map(int, input().split(" "))
    answer = []
    for num in numbers:
        properties = {}
        bin_repr = bin(num)[2:]
        properties["digits"] = len(bin_repr)
        properties["units"] = bin_repr.count("1")
        properties["zeros"] = bin_repr.count("0")
        answer.append(properties)
    print(answer)


if __name__ == '__main__':
    task_o()
