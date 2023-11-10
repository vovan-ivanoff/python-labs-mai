"""задание b:Генератор матриц"""


def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for k in range(size)] for i in range(size)]
    else:
        return [[value for k in range(size[0])] for i in range(size[1])]
