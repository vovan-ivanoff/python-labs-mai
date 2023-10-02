def task_g():
    """задание g: На старт! Внимание! Марш!"""
    for number in range(int(input())):
        countdown = 3 + number
        while countdown > 0:
            print(f"До старта {countdown} секунд(ы)")
            countdown -= 1
        print(f"Старт {number + 1}!!!")


if __name__ == '__main__':
    task_g()
