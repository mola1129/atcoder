n, a, b = map(int, input().split())
cnt = n // (a + b)
ans = a * cnt + min(n - (a + b) * cnt, a)
print(ans)
