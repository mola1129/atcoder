x, y = map(int, input().split())
ans = float('inf')
if x <= y:
    ans = min(ans, y - x)
if (-1) * x <= y:
    ans = min(ans, y + x + 1)
if x <= (-1) * y:
    ans = min(ans, -y - x + 1)
if (-1) * x <= (-1) * y:
    ans = min(ans, -y + x + 2)
print(ans)
