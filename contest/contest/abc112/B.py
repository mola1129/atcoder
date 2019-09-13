n, t = map(int, input().split())
c = []
for _ in range(n):
    ct = tuple(map(int, input().split()))
    if ct[1] <= t:
        c.append(ct[0])
if c != []:
    c.sort()
    print(c[0])
else:
    print("TLE")
