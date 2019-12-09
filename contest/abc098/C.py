n = int(input())
s = input()
# 左からi文字目までに存在するW,Eの累積和
east = [0] * (n + 1)
west = [0] * (n + 1)
for i in range(n):
    east[i + 1] = east[i]
    west[i + 1] = west[i]
    if s[i] == 'E':
        east[i + 1] += 1
    else:
        west[i + 1] += 1

ans = float('inf')
for i in range(1, n):
    tmp = west[i - 1] + east[-1] - east[i]
    ans = min(ans, tmp)
# N番目
ans = min(ans, west[n - 1])
print(ans)
