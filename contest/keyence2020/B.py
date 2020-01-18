n = int(input())
robots = []
for _ in range(n):
    xi, li = map(int, input().split())
    robots.append((xi - li, xi + li))
robots.sort(key=lambda x: x[1])
ans = 0
pre_r = -float('inf')
for l, r in robots:
    if pre_r <= l:
        ans += 1
        pre_r = r
print(ans)
