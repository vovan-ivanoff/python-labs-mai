def task_e():
    "задание e: Максимальное среднее"
    avgs = []
    for _ in range(int(input())):
        posl = []
        while (num := input()) != "next":
            posl.append(float(num))
        avgs.append(sum(posl) / len(posl))
    print(f"{max(avgs):.2f}")


if __name__ == "__main__":
    task_e()
