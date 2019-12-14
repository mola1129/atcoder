n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
cnt = [0] * (200000)
for i in range(n):
    cnt[a[i] - 1] += 1
cnt.sort(reverse=True)
kinds = 200000 - cnt.count(0)
if kinds <= k:
    print(0)
else:
    for i in range(kinds - k):
        ans += cnt[kinds - 1 - i]
    print(ans)
