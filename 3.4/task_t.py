def solver(action: dict):
    """решатель"""
    ...


def task_t():
    """задание t: таблица истинности 3"""
    vyrazhenie = input().replace('(', '( ').replace(")"," )").split()
    variables = set()
    pending_actions = {}
    for idx, token in enumerate(reversed(vyrazhenie)):
        if token.isupper():
            variables.add(token)
        else:
            if token == "not":
                ...
            if token == "and":
                ...
            if token == "or":
                ...
            if token == "^":
                ...
            if token == "->":
                ...
            if token == "~":
                ...
    print(vyrazhenie, variables)


if __name__ == '__main__':
    task_t()
