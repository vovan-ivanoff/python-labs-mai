def task_c():
    """задание c: Длины всех слов"""
    sentence = input()
    print([len(word) for word in sentence.split()])
# [len(word) for word in sentence.split()]


if __name__ == '__main__':
    task_c()
