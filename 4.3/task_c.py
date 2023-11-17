"""задание c: Многочлен N-ой степени"""


def make_equation(*coefs):
    if len(coefs) == 1:
        return f"{coefs[0]}"
    return f"({make_equation(*coefs[:-1:])}) * x + {coefs[-1]}"
