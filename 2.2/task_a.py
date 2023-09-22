def task_a():
    """Просто здравствуй, просто как дела"""
    name = input()
    state = input()
    print("Как Вас зовут?")
    print(f"Здравствуйте, {name}!")
    print("Как дела?")
    if state == "хорошо":
        print("Я за вас рада!")
    else:
        print("Всё наладится!")


if __name__ == '__main__':
    task_a()
