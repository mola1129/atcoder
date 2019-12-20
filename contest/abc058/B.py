o = input()
e = input()
ans = ''
for i in range(min(len(o), len(e))):
    ans += o[i]
    ans += e[i]
if len(o) > len(e):
    ans += o[len(o) - 1]
if len(o) < len(e):
    ans += o[len(e) - 1]
print(ans)
