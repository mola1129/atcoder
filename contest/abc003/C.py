n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
ans = 0
for i in range(k):
    ans = (ans + r[-k + i]) / 2
print(ans)
