q, h, s, d = map(int, input().split())
n = int(input())
liter = min(4 * q, 2 * h, s)
ans = min(liter * n, n // 2 * d + n % 2 * liter)
print(ans)
