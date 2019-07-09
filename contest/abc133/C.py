l, r = map(int, input().split())
l_mod = l % 2019
r_mod = r % 2019
area = r_mod - l_mod
ans = -1
if area > 0:
    ans = l_mod * (l_mod + 1) % 2019
else:
    ans = 0
print(ans)
