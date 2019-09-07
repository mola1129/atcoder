n, q = map(int, input().split())
s = input()
# 累積和: i文字目までに"AC"がいくつ含まれているか
cum = [0] * (n + 1)
for i in range(2, n + 1):
    cum[i] = cum[i - 1]
    if s[i - 2:i] == "AC":
        cum[i] += 1

ans = [0] * q
for i in range(q):
    l, r = map(int, input().split())
    # 指定された区間の"AC"の数
    ans[i] = cum[r] - cum[l]
print(*ans, sep='\n')
