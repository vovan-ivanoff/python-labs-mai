def task_l():
    """задание l: Меню питания"""
    kashi = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")
    for i in range(int(input())):
        print(kashi[i % 5])


if __name__ == '__main__':
    task_l()
