def task_s():
    """задание s: Польский калькулятор"""
    stack = []
    tokens = input().split(" ")
    for token in tokens:
        if token == "+":
            result = stack[-2] + stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "-":
            result = stack[-2] - stack[-1]
            stack.pop()
            stack[-1] = result
        elif token == "*":
            result = stack[-2] * stack[-1]
            stack.pop()
            stack[-1] = result
        else:
            stack.append(int(token))
    print(stack[-1])


if __name__ == '__main__':
    task_s()
