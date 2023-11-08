import json


def task_k():
    """задание k: Файловая статистика 2.0"""
    file = input()
    outfile = input()
    nums = []
    with open(file, "r", encoding="UTF-8") as f:
        for line in f.readlines():
            nums += [*map(int, line.split())]
    result = {}
    result["count"] = len(nums)
    result["positive_count"] = len([x for x in nums if x > 0])
    result["min"] = min(nums)
    result["max"] = max(nums)
    result["sum"] = sum(nums)
    result["average"] = float(f"{(sum(nums) / len(nums)):.2f}")
    with open(outfile, "w", encoding="UTF-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    task_k()
