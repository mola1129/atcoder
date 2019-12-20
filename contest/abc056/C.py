x = int(input())
candidate = [1] * (10 ** 5 + 1)
ans = 0
for i in range(1, 10 ** 5 + 1):
    candidate[i] = candidate[i - 1] + i + 1
    if candidate[i] > 10 ** 9:
        break
for i in range(len(candidate)):
    if x <= candidate[i]:
        print(i + 1)
        exit()
