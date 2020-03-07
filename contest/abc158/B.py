n, a, b = map(int, input().split())
c = a + b
cnt = n // c
ans = a * cnt + min(n % c, a)
print(ans)
