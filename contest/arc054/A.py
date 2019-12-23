L, X, Y, S, D = map(int, input().split())
ans = float('inf')
if S <= D:
    ans = (D - S) / (X + Y)
    if Y - X > 0:
        ans = min(ans, (S + L - D) / (Y - X))
else:
    ans = (D - S + L) / (X + Y)
    if Y - X > 0:
        ans = min(ans, (S - D) / (Y - X))
print(ans)
