total = int(input())
# おつり
change = 1000 - total
coins = (500, 100, 50, 10, 5, 1)
ans = 0
for price in coins:
    # 大きい硬貨から引けるだけ引く
    while (change - price) >= 0:
        change -= price
        ans += 1
print(ans)
