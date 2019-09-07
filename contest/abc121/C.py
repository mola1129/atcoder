n, m = map(int, input().split())
ans = 0
# (ドリンクの単価, 購入可能本数)
shop = [tuple(map(int, input().split())) for _ in range(n)]
# 安い店から購入するのが最適
shop.sort()
for price, num in shop:
    num = min(m, num)
    ans += price * num
    m -= num
print(ans)
