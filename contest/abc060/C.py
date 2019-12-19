N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T
for i in range(N - 1):
    ans += min(T, t[i + 1] - t[i])
print(ans)
