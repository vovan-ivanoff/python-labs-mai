def task_i():
    """задание i: Преобразование в строку"""
    numbers = [3, 1, 2, 3, 2, 2, 1]
    print(" - ".join(map(str, sorted(set(numbers)))))
# " - ".join(map(str, sorted(set(numbers))))


if __name__ == '__main__':
    task_i()
