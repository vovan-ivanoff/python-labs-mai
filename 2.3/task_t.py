def task_t():
    """задание t: Хайпанём немножечко"""
    blocks = []
    prev_hash = 0
    for _ in range(int(input())):
        blocks.append(int(input()))
    for block in blocks:
        block_hash = block % 256
        block_random = (block // 256) % 256
        block_message = block // 256 ** 2
        calc_hash = (37 * (block_message + block_random + prev_hash)) % 256
        if calc_hash > 100 or calc_hash != block_hash:
            print(blocks.index(block))
            break
        else:
            prev_hash = calc_hash
    else:
        print(-1)


if __name__ == '__main__':
    task_t()
