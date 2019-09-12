n = int(input())
h = list(map(int, input().split()))
ans = 0
# 水やり = (l<=i<=r)区間のh[i]を-1すると考える
# hの要素が全て0になるまで繰り返す
while sum(h) != 0:
    # 初期化
    left = float("inf")
    right = float("inf")
    # 連続した自然数の区間を見つける
    # 左端番号leftの設定
    for i in range(n):
        if h[i] > 0:
            left = i
            break
    # 右端番号rightの設定
    for j in range(i + 1, n):
        if h[j] <= 0:
            right = j
            break
    if right == float("inf"):
        right = n
    # 見つけた区間の全ての要素を-1
    for i in range(left, right):
        h[i] -= 1
    ans += 1
print(ans)
