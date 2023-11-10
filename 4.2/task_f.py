"""задание f: Модернизация системы вывода"""
in_stock = {"coffee": 4, "milk": 4, "cream": 0}


def order(*wishes):
    coffes = {"Эспрессо": [1, 0, 0],
              "Капучино": [1, 0, 3],
              "Макиато": [2, 0, 1],
              "Кофе по-венски": [1, 2, 0],
              "Латте Макиато": [1, 1, 2],
              "Кон Панна": [1, 1, 0]}
    for w in wishes:
        cof = coffes[w][0]
        cream = coffes[w][1]
        milk = coffes[w][2]
        if cof <= in_stock["coffee"] and\
           cream <= in_stock["cream"] and\
           milk <= in_stock["milk"]:
            in_stock["coffee"] -= cof
            in_stock["cream"] -= cream
            in_stock["milk"] -= milk
            return w
    return "К сожалению, не можем предложить Вам напиток"
