"""задание e: Числовая строка"""


def split_numbers(inp: str):
    return tuple(map(int, inp.split()))
