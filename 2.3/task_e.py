def task_e():
    """задание e: Внимание! Акция!"""
    total = 0
    while (price := float(input())) != 0:
        if price >= 500:
            total += 0.9 * price
        else:
            total += price
    print(total)


if __name__ == '__main__':
    task_e()
