from sys import stdin


def task_e():
    """задание e: А роза упала на лапу Азора 6.0"""
    words = []
    for line in stdin:
        words += [*line.split()]
    for word in sorted(set(words)):
        if word.lower() == word.lower()[::-1]:
            print(word)


if __name__ == '__main__':
    task_e()
