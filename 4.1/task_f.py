"""задание f: Модернизация системы вывода"""
used = []


def modern_print(inp: str):
    if inp not in used:
        print(inp)
        used.append(inp)
