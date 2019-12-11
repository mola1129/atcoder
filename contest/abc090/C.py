n, m = map(int, input().split())
if n == 1 or m == 1:
    print(max(n * m - 2, 1))
else:
    print((n - 2) * (m - 2))
