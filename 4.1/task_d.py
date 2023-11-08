"""задание d: Имя of the month"""


def month(num: int, lang: str):
    ru_m = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
            "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    en_m = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]
    if lang == "ru":
        return ru_m[num - 1]
    elif lang == "en":
        return en_m[num - 1]
