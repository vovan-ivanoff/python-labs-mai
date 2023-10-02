def task_j():
    """задание j: Мы делили апельсин"""
    number_of_dolka = int(input())
    print("А Б В")
    for a in range(1, number_of_dolka - 1):
        for b in range(1, number_of_dolka - 1):
            if number_of_dolka - (a + b) < 1:
                continue
            print(a, b, number_of_dolka - (a + b))


if __name__ == '__main__':
    task_j()
