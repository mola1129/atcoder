s = input()
n = len(s)
formulas = s.split('+')
ans = 0
for f in formulas:
    for i in range(len(f)):
        if f[i] == '0':
            break
        if i == len(f) - 1:
            ans += 1
print(ans)
