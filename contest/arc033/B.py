import bisect
na, nb = map(int, input().split())
a = list(set(map(int, input().split())))
b = list(set(map(int, input().split())))
b.sort()
upper = 0
for i in range(na):
    index = bisect.bisect_left(b, a[i])
    if index < nb and b[index] == a[i]:
        upper += 1
lower = len(a) + len(b) - upper
print(upper / lower)
