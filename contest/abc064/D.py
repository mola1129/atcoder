n = int(input())
s = input()
cnt = 0
ans = ''
for i in range(n):
    if s[i] == '(':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ans += '('
        cnt = 0
ans += s
if cnt > 0:
    for i in range(cnt):
        ans += ')'
print(ans)
