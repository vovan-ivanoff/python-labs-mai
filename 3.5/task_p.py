from sys import stdin


def task_p():
    """задание p: Найдётся всё 3.0"""
    query = input()
    files = []
    flag = False
    for line in stdin:
        files.append(line.strip())
    for file in files:
        with open(file, "r", encoding="UTF-8") as f:
            data = f.read()
        if query.lower() in " ".join(data.split()).lower():
            print(file)
            flag = True
    if not flag:
        print("404. Not Found")


if __name__ == '__main__':
    task_p()
