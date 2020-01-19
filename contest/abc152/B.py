t = list(input().split())
t.sort()
ans = ''
for i in range(int(t[1])):
    ans += t[0]
print(ans)
