A, B, X = map(int, input().split())
# 桁数の決定
dn = -1
for i in range(10):
    n = 1 * (10 ** i)
    if X < (A * n + B * (i + 1)):
        dn = i
        break
if dn == -1:
    print(10 ** 9)
elif dn == 0:
    print(0)
else:
    ans = (X - B * dn) // A
    if len(str(ans)) > dn:
        ans -= 1
    print(ans)
