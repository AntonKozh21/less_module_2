print("На тебя уже двигаются шипы, а значит игра началась."
      " Какое число ты видишь на первом камне?\n"
      "Я помогу тебе подобрать нужные числа для выхода, скорее.")
n = int(input("Введите число от 3 до 20"))
result = []
for j in range(1, 21):
    for k in range(1, 21):
        _ = j + k
        if n == _ and j < k:
            result.append([j, k])
        elif n % _ == 0 and j < k:
            result.append([j, k])
print(f"{n} - {result}")
