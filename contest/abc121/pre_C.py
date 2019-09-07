n, m = map(int, input().split())
a = [0] * (n + 1)
b = [0] * (n + 1)
total = [0] * (n + 1)
ans = 0

# 安い店から選ぶ方法が最適
shop = [tuple(map(int, input().split())) for _ in range(n)]
shop.sort()

for i in range(1, n + 1):
    a_i, b_i = shop[i - 1]
    # 累積和を作っておく
    # b[i]: i番目の店まで利用した際に購入できる栄養ドリンクの最大本数
    # total[i]: i番目の店まで利用した際に支払うお金の最大値
    b[i] = b[i - 1]
    total[i] = total[i - 1]
    b[i] += b_i
    total[i] += a_i * b_i

    # a[i]: i番目の店の栄養ドリンクの単価
    a[i] = a_i

for i in range(1, n + 1):
    if m <= b[i]:
        m = m - b[i - 1]
        # 足りない分を追加で計算
        ans = total[i - 1] + a[i] * m
        break
print(ans)
