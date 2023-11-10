"""задание e: Подготовка данных"""


def to_string(*elems, sep=" ", end="\n"):
    return sep.join(map(str, elems)) + end
