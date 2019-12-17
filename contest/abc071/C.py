import collections
dd = collections.defaultdict(int)
n = int(input())
a = list(map(int, input().split()))
candidate = []
for i in range(n):
    dd[str(a[i])] += 1
for k in dd.keys():
    if dd[k] >= 2:
        candidate.append(int(k))
    if dd[k] >= 4:
        candidate.append(int(k))
candidate.sort(reverse=True)
if len(candidate) < 2:
    print(0)
else:
    print(candidate[0] * candidate[1])
