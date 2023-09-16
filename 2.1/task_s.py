"""Задание S"""


def task_s():
    nazv = input()
    cena = int(input())
    ves = int(input())
    babki = int(input())
    
    result = "Чек".center(35, "=") + "\n" + \
             "Товар:" + nazv.rjust(29) + "\n" + \
             "Цена:" + (str(ves) + "кг * " + str(cena) + "руб/кг").rjust(30) + \
             "\n" + \
             "Итого:" + (str(ves * cena) + "руб").rjust(29) + "\n" + \
             "Внесено:" + (str(babki) + "руб").rjust(27) + "\n" + \
             "Сдача:" + (str(babki - ves * cena) + "руб").rjust(29) + "\n" + \
             "=" * 35
    print(result)


if __name__ == '__main__':
    task_s()
