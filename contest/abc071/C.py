from collections import Counter
n = int(input())
ctr = Counter(list(map(int, input().split())))
side = []
for k in sorted(ctr.keys(), reverse=True):
    if ctr[k] >= 4:
        side.append(k)
        side.append(k)
    elif ctr[k] >= 2:
        side.append(k)
print(side[0] * side[1] if len(side) >= 2 else 0)
