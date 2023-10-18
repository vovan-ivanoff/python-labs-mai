def task_h():
    """задание h: Аббревиатура"""
    string = "Российская Федерация"
    print("".join([i[0].upper() for i in string.split()]))
# "".join([i[0].upper() for i in string.split()])


if __name__ == '__main__':
    task_h()
