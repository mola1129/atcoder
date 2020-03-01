n, m, k = map(int, input().split())
friend = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friend[a - 1].append(b - 1)
    friend[b - 1].append(a - 1)
block = [[] for _ in range(n)]
for _ in range(k):
    c, d = map(int, input().split())
    block[c - 1].append(d - 1)
    block[d - 1].append(c - 1)
