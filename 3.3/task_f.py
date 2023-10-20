def task_f():
    """задание f: Буквенная статистика"""
    text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
    print({i: text.lower().count(i) for i in text.lower() if i.isalpha()})
# {i: text.lower().count(i) for i in text.lower() if i.isalpha()}


if __name__ == '__main__':
    task_f()
