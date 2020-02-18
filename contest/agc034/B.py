s = input().replace('BC', 'D')
cnt = 0
ans = 0
for c in s:
    if c == 'A':
        cnt += 1
    elif c == 'D':
        ans += cnt
    else:
        cnt = 0
print(ans)
