from sys import stdin


def task_b():
    """задание b: Средний рост"""
    deltas = []
    for line in stdin:
        deltas.append(int(line.split()[2]) - int(line.split()[1]))
    print(round(sum(deltas) / len(deltas)))


if __name__ == '__main__':
    task_b()
