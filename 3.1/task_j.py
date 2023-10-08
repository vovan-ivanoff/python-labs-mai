def task_j():
    """задание j: Частотный анализ на минималках"""
    input_str = ""
    max_count = 0
    bukva = "f"
    while (data := input()) != "ФИНИШ":
        input_str += data.lower()
    chars = set(input_str)
    chars.discard(" ")
    chars = sorted(list(chars))
    for char in reversed(chars):
        count = input_str.count(char)
        if count >= max_count:
            max_count = count
            bukva = char
    print(bukva)


if __name__ == '__main__':
    task_j()
