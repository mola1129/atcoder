m, d = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    for j in range(1, d + 1):
        ten = j // 10
        one = j % 10
        if ten >= 2 and one >= 2 and i == ten * one:
            ans += 1
print(ans)
