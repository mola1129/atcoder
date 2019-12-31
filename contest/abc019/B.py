s = input()
n = len(s)
pre = s[0]
cnt = 1
ans = ''
for i in range(1, n):
    if s[i] == pre:
        cnt += 1
    else:
        ans += pre + str(cnt)
        pre = s[i]
        cnt = 1
    if i == n - 1:
        ans += s[i] + str(cnt)
print(ans)
