import random
list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(list_)
result_base = []
for j in range(1, 21):
    for k in range(1, 21):
        _ = j + k
        if n == _ and j < k:
            result_base.append([j, k])
        elif n % _ == 0 and j < k:
            result_base.append([j, k])
print(n)
result = ''
for pair in result_base:
    result += f'{pair[0]} {pair[1]} '
result = result.replace(" ", "")
print(result.strip())
