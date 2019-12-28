import fractions
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
g = a[0]
for i in range(n):
    g = fractions.gcd(g, a[i])
if k % g == 0 and k <= a[-1]:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
