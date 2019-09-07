import fractions
n = int(input())
a = list(map(int, input().split()))
# A_iを消した場合の最大公約数
ans = [0] * n
# L[i]: A_1 ~ A_(i-1)までの最大公約数
L = [0] * n
# R[i]: A_(i+1) ~ A_Nまでの最大公約数
R = [0] * n
for i in range(1, n):
    L[i] = fractions.gcd(a[i - 1], L[i - 1])
    R[n - 1 - i] = fractions.gcd(a[n - i], R[n - i])
for i in range(0, n):
    ans[i] = fractions.gcd(L[i], R[i])
ans.sort()
print(ans[n - 1])
