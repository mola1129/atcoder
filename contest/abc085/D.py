import math
n, h = map(int, input().split())
a = []
b = []
ans = 0
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
a.sort(reverse=True)
b.sort(reverse=True)
max_a = a[0]
for i in range(n):
    if b[i] >= max_a:
        h -= b[i]
        ans += 1
    else:
        break
    if h <= 0:
        break
if h > 0:
    ans += math.ceil(h / max_a)
print(ans)
