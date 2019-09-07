n = int(input())
t = [int(input()) for _ in range(n)]
ans = 100000
for i in range(2 ** n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        if (i >> j) & 1:
            sum1 += t[j]
        else:
            sum2 += t[j]
    ans = min(ans, max(sum1, sum2))
print(ans)
