n = int(input())
ans = 0
train = [tuple(map(int, input().split())) for _ in range(n - 1)]
for i in range(n - 1):
    total = train[i][0] + train[i][1]
    for j in range(i + 1, n - 1):
        diff = total - train[j][1]
        if diff <= 0:
            total = train[j][1]
        elif diff % train[j][2] != 0:
            total += train[j][2] - diff % train[j][2]
        total += train[j][0]
    print(total)
print(0)
