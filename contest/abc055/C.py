n, m = map(int, input().split())
ans = 0
if n <= m // 2:
    ans += n
    m -= 2 * n
    ans += m // 4
else:
    ans += m // 2
print(ans)
