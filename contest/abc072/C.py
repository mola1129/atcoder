import collections
n = int(input())
a = list(map(int, input().split()))
ans = 0
dd = collections.defaultdict(int)
for i in range(n):
    dd[str(a[i])] += 1
for i in range(1, 10 ** 5 - 1):
    tmp = dd[str(i - 1)] + dd[str(i)] + dd[str(i + 1)]
    ans = max(ans, tmp)
print(ans)
