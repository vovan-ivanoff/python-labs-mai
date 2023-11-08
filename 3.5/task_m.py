import json
from sys import stdin


def task_m():
    """задание m: Обновление данных"""
    data = {}
    with open((filename := input()), "r", encoding="UTF-8") as f:
        data = json.load(f)
    for line in stdin:
        key, value = line.strip().split(" == ")
        data[key] = value
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    task_m()
