n = int(input())
a = []
b = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
cnt = 0
for i in range(n - 1, -1, -1):
    rest = (a[i] + cnt) % b[i]
    if rest != 0:
        cnt += b[i] - rest
print(cnt)
