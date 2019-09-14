import fractions
n = int(input())
a = list(map(int, input().split()))
ans = 0
# 最大公約数を求める
for i in range(n - 1):
    ans = fractions.gcd(a[i], a[i + 1])
    a[i + 1] = ans
print(ans)
