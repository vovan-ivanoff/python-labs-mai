def task_r():
    """задание r: RLE"""
    data = input()
    counter = 0
    prev_char = data[0]
    while data:
        if prev_char == data[0]:
            counter += 1
            data = data[1:]
        else:
            print(prev_char, counter)
            prev_char = data[0]
            counter = 1
            data = data[1:]
    print(prev_char, counter)


if __name__ == '__main__':
    task_r()
