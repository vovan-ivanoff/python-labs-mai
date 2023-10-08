def task_t():
    """задание t: Польский калькулятор — 2"""
    stack = []
    tokens = input().split(" ")
    for token in tokens:
        if token == "+":  # сложение
            result = stack[-2] + stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "-":  # вычитание
            result = stack[-2] - stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "*":  # умножение
            result = stack[-2] * stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "/":  # деление
            result = stack[-2] // stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "~":  # инверсия
            result = -1 * stack[-1]
            stack[-1] = result
        elif token == "!":  # Факториал
            result = 1
            for i in range(stack[-1]):
                result *= (i + 1)
            stack[-1] = result
        elif token == "#":  # Клонирование
            stack.append(stack[-1])
        elif token == "@":  # своп
            (stack[-3], stack[-2], stack[-1]) =\
                (stack[-2], stack[-1], stack[-3])
        else:
            stack.append(int(token))
    print(stack[-1])


if __name__ == '__main__':
    task_t()
