def task_t():
    """задание t: Простая задача 4.0"""
    chisla = sorted(set(map(int, input().split("; "))))
    for chislo in chisla:
        result = set()
        for chislo_2 in chisla:
            a = chislo
            b = chislo_2
            while a != b:
                if a > b:
                    a -= b
                if a < b:
                    b -= a
            if a == 1:
                result.add(chislo_2)
        if not result:
            continue
        print(chislo, end=" - ")
        print(", ".join(map(str, sorted(result))))


if __name__ == '__main__':
    task_t()
