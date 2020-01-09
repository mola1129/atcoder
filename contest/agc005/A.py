x = input()
ans = 0
cnt = 0
for s in x:
    if s == 'S':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ans += 1
        cnt = 0
ans += cnt
print(ans)
