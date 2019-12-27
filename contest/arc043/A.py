n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
if s[0] == s[-1]:
    print(-1)
    exit()
else:
    p = b / (s[-1] - s[0])
    total = 0
    for i in range(n):
        total += p * s[i]
    q = (a * n - total) / n
    print(p, q)
