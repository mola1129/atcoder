a, b, x = map(int, input().split())
ans = 0
if a % x != 0:
    a -= a % x
    ans -= 1
ans += (b - a) // x + 1
print(ans)
