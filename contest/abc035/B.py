s = list(input())
t = int(input())
xy = [0, 0]
cnt = 0
for i in range(len(s)):
    if s[i] == 'U':
        xy[1] += 1
    if s[i] == 'D':
        xy[1] -= 1
    if s[i] == 'L':
        xy[0] -= 1
    if s[i] == 'R':
        xy[0] += 1
    if s[i] == '?':
        cnt += 1
if t == 1:
    print(abs(xy[0]) + abs(xy[1]) + cnt)
else:
    ans = abs(xy[0]) + abs(xy[1]) - cnt
    if ans < 0:
        ans %= 2
    print(ans)
