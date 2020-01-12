n, k, m = map(int, input().split())
a = list(map(int, input().split()))
total = m * n
if total - sum(a) <= k:
    print(max(0, total - sum(a)))
else:
    print(-1)
