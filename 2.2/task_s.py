def task_s():
    """задание s: Автоматизация безопасности"""
    x = float(input())
    y = float(input())
    if ((x >= 0 and y >= 0) and (x ** 2 + y ** 2 <= 25)) or\
       ((x < 0 and y > 0 and y <= 5) and (y < x * 5 / 3 + 35 / 3)) or\
       ((y < 0) and (y >= 0.25 * (x - 5) * (x + 7))):
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")


if __name__ == '__main__':
    task_s()