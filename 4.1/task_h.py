"""задание h: А роза упала на лапу Азора 7.0"""


def is_palindrome(inp: any):
    return str(inp) == str(inp)[::-1] if isinstance(inp, int)\
           else inp == inp[::-1]
