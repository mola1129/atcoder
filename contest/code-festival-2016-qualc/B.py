k, t = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * t
for i in range(t):
    cnt[i] += sum(a[:i])
    if i != t - 1:
        cnt[i] += sum(a[i + 1:])
ans = -1
for i in range(t):
    if a[i] > cnt[i]:
        ans += a[i] - cnt[i]
print(max(ans, 0))
