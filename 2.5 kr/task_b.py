def task_b():
    "задание b: Условный калькулятор"
    action = input()
    num1 = int(input())
    num2 = int(input())
    if "sum" in action:
        print(num1 + num2)
    elif "sub" in action:
        print(num1 - num2)
    elif "mult" in action:
        print(num1 * num2)
    elif "div" in action:
        print(num1 // num2)


if __name__ == "__main__":
    task_b()
