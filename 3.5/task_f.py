def task_f():
    """задание f: Транслитерация 2.0"""
    transiteration_dict = {"а": "a", "б": "b", "в": "v", "г": "g",
                           "д": "d", "е": "e", "ё": "e", "ж": "zh",
                           "з": "z", "и": "i", "й": "i", "к": "k",
                           "л": "l", "м": "m", "н": "n", "о": "o",
                           "п": "p", "р": "r", "с": "s", "т": "t",
                           "у": "u", "ф": "f", "х": "kh", "ц": "tc",
                           "ч": "ch", "ш": "sh", "щ": "shch", "ы": "y",
                           "э": "e", "ю": "iu", "я": "ia", "ь": "",
                           "ъ": ""}
    russian = ""
    with open("cyrillic.txt", "r", encoding="UTF-8") as f:
        russian = f.read()
    result = ""
    for letter in russian:
        if letter.lower() in transiteration_dict:
            if letter.isupper():
                result += transiteration_dict[letter.lower()].capitalize()
            else:
                result += transiteration_dict[letter.lower()]
        else:
            result += letter
    with open("transliteration.txt", "w", encoding="UTF-8") as f:
        f.write(result)


if __name__ == '__main__':
    task_f()
