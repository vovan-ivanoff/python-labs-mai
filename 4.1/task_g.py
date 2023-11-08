"""задание g: Шахматный «обед»"""


def can_eat(cur: tuple, eat: tuple):
    x1, y1 = cur
    x2, y2 = eat
    return (x1 + 2 == x2 and y1 + 1 == y2) or\
           (x1 + 2 == x2 and y1 - 1 == y2) or\
           (x1 - 2 == x2 and y1 + 1 == y2) or\
           (x1 - 2 == x2 and y1 - 1 == y2) or\
           (y1 + 2 == y2 and x1 + 1 == x2) or\
           (y1 + 2 == y2 and x1 - 1 == x2) or\
           (y1 - 2 == y2 and x1 + 1 == x2) or\
           (y1 - 2 == y2 and x1 - 1 == x2)
