n = int(input())
p = list(map(int, input().split()))
tmp = float('inf')
ans = 0
for i in range(n):
    if tmp >= p[i]:
        ans += 1
    tmp = min(tmp, p[i])
print(ans)
