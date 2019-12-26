n = int(input())
s = [input() for _ in range(n)]
cnt_a = 0
cnt_b = 0
cnt_ba = 0
ans = 0
for i in range(n):
    ans += s[i].count('AB')
    if s[i][0] == 'B' and s[i][-1] == 'A':
        cnt_ba += 1
        continue
    if s[i][0] == 'B':
        cnt_b += 1
    if s[i][-1] == 'A':
        cnt_a += 1
if cnt_ba == 0:
    ans += min(cnt_a, cnt_b)
else:
    if cnt_a == 0 and cnt_b == 0:
        ans += max(cnt_ba - 1, 0)
    else:
        ans += cnt_ba + min(cnt_a, cnt_b)
print(ans)
