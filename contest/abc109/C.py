import fractions
N, X = map(int, input().split())
x = list(map(int, input().split()))
# 全て回るには距離が共通の倍数でないとダメ
# 最大の正整数は最大公約数
ans = abs(X - x[0])
for i in range(1, N):
    ans = fractions.gcd(ans, abs(X - x[i]))
print(ans)
