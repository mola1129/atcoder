import collections
n = int(input())
dd = collections.defaultdict(int)
for i in range(n):
    dd[input()] += 1
score = 0
ans = ''
for k in dd.keys():
    if dd[k] >= score:
        score = dd[k]
        ans = k
print(ans)
