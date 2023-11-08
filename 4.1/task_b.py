"""задание b: Функциональный НОД"""


def gcd(a: int, b: int):
    while a != 0:
        a, b = b % a, a
    return b
