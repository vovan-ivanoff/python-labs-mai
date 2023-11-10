"""В эфире рубрика «Эксперименты»"""
values = []


def enter_results(*inp):
    global values
    values += inp


def get_sum():
    """nihuya"""
    return round(sum(values[::2]), 2), round(sum(values[1::2]), 2)


def get_average():
    """hui"""
    return round(2 * sum(values[::2]) / len(values), 2), \
        round((2 * sum(values[1::2]) / len(values)), 2)
