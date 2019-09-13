n,m = map(int, input().split())
DIV = 10**9+7
a = [0]*(n+1)
dp = [0]*(n+1)
dp[0] = 1
for _ in range(m):
    broken = int(input())
    a[broken] = 1
for i in range(1,n+1):
    dp[i]=(dp[i-1]+dp[i-2]) % DIV
    if a[i] == 1:
        dp[i] = 0
print(dp[n])
print(dp)
