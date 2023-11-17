"""задание b:Рекурсивный сумматор цифр"""


def recursive_digit_sum(num):
    rsum = 0
    if num == 0:
        return rsum
    return num % 10 + recursive_digit_sum(num // 10)
