n = int(input())
ans = 0
for _ in range(n):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        ans += 380000.0 * x
    else:
        ans += x
print(ans)
