from sys import stdin
import json


def task_o():
    """задание o: Поставь себя на моё место"""
    result = 0
    test_number = 0
    answers = [line.strip() for line in stdin.readlines()]
    with open("scoring.json", "r", encoding="UTF-8") as f:
        scoring_dict = json.load(f)
    for group in scoring_dict:
        price = group["points"] // len(group["tests"])
        for test in group["tests"]:
            if test["pattern"] == answers[test_number]:
                result += price
            test_number += 1
    print(result)


if __name__ == '__main__':
    task_o()
