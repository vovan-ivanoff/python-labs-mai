"""Однотипность не порок"""


def same_type(f):

    def decorated(*args):
        for arg in args[1::]:
            if type(args[0]) is not type(arg):
                print("Обнаружены различные типы данных")
                return
        return f(*args)
    return decorated
