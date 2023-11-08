def task_i():
    """задание i: Файловая чистка"""
    infile = input()
    outfile = input()
    with open(infile, "r", encoding="UTF-8") as f:
        lines = [line.rstrip("\n") for line in f.readlines()
                 if line.rstrip("\n") != ""]
    for idx, line in enumerate(lines):
        lines[idx] = line.replace("\t", "").split()
    lines = [d for d in lines if any(d)]
    with open(outfile, "w", encoding="UTF-8") as f:
        for line in lines:
            f.write(" ".join(line) + "\n")


if __name__ == '__main__':
    task_i()
