import json
from sys import stdin


def task_e():
    "задание e: Алфавитная статистика"
    words = []
    even_letters = []
    out_dict = {}
    for line in stdin:
        words.append(line.strip().lower())
        even_letters += line.strip().lower()[1::2]
    for word in words:
        for check_letter in even_letters:
            if check_letter in word[1::2]:
                if check_letter not in out_dict:
                    out_dict[check_letter] = [word]
                else:
                    out_dict[check_letter].append(word)
    for key in out_dict:
        out_dict[key] = list(sorted(set(out_dict[key])))

    with open("result.json", "w", encoding="UTF-8") as f:
        json.dump(out_dict, f)


if __name__ == "__main__":
    task_e()
