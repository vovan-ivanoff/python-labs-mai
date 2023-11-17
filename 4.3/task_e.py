"""задание e: Накопление результата"""


def result_accumulator(f):
    accumulator = []

    def decorated(*args, method="accumulate"):
        nonlocal accumulator
        if method == "accumulate":
            accumulator.append(f(*args))
            return None
        if method == "drop":
            accumulator.append(f(*args))
            temp = accumulator.copy()
            accumulator.clear()
            return temp
    return decorated
