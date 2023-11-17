"""задание j: "Выпрямление" списка"""


def make_linear(arr: list):
    accumulate = []
    for arg in arr:
        if isinstance(arg, list):
            accumulate += make_linear(arg)
        else:
            accumulate.append(arg)
    return accumulate
