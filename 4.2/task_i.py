"""задание i: Чётная фильтрация"""


print(*filter(lambda x: sum(map(int, str(x))) % 2 == 0,
              (32, 64, 128, 256, 512)))
