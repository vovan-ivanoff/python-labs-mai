"""задание c: Функциональный нод 2.0"""


def gcd(*numbers):
    numbers = sorted(list(numbers))
    prev_nod = numbers[-1]
    for num in numbers:
        while prev_nod != 0:
            prev_nod, num = num % prev_nod, prev_nod
        prev_nod = num
    return prev_nod
