def task_p():
    """задание p: Зайка - 10"""
    surrounding = set()
    while (land := input()) != "":
        temp_list = land.split(" ")
        for i, _ in enumerate(temp_list):
            if temp_list[i] == "зайка":
                if len(temp_list) == 1:
                    break
                if i == 0:
                    surrounding.add(temp_list[i + 1])
                elif i == len(temp_list) - 1:
                    surrounding.add(temp_list[i - 1])
                else:
                    surrounding.add(temp_list[i - 1])
                    surrounding.add(temp_list[i + 1])
            else:
                continue
    print("\n".join(surrounding))


if __name__ == '__main__':
    task_p()
