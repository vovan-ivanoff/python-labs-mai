"""Задание F"""


def task_f():
    nazv = input()
    cena = int(input())
    ves = int(input())
    dengi = int(input())
    print(f"Чек\n{nazv} - {ves}кг - {cena}руб/кг\nИтого: {str(cena * ves)}руб\n\
Внесено: {dengi}руб\nСдача: {str(dengi - cena * ves)}руб")


if __name__ == '__main__':
    task_f()
