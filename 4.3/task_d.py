"""задание d: Декор результата"""


def answer(f):
    def decorated(*args, **kwargs):
        return f"Результат функции: {str(f(*args, **kwargs))}"
    return decorated
