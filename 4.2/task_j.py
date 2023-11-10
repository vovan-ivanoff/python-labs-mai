"""задание j: Ключевой секрет"""


def secret_replace(inp_str, **replaces):
    out_str = ""
    count = {}
    for sym in inp_str:
        if sym in replaces.keys():
            if sym not in count.keys():
                count[sym] = 1
            else:
                count[sym] += 1
            out_str += replaces[sym][(count[sym] - 1) % len(replaces[sym])]
        else:
            out_str += sym
    return out_str
