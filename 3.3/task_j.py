def task_j():
    """задание j: RLE наоборот"""
    rle = [('a', 2), ('b', 3), ('c', 1)]
    print("".join([sym * amo for sym, amo in rle]))
# "".join([sym * amo for sym, amo in rle])


if __name__ == '__main__':
    task_j()
