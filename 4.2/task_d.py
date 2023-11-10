"""задание d: Имя of the month 2.0"""


def month(num: int, lang="ru"):
    ru_m = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
            "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    en_m = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]
    if lang == "ru":
        return ru_m[num - 1]
    elif lang == "en":
        return en_m[num - 1]
