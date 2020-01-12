n = int(input())
s = []
t = []
for _ in range(n):
    si, ti = input().split()
    ti = int(ti)
    s.append(si)
    t.append(ti)
x = input()
ans = sum(t)
for i in range(n):
    ans -= t[i]
    if s[i] == x:
        break

print(ans)
