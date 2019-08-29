n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
# 尺取り法
right = 0
total = 0
# 左端を固定
for left in range(n):
    # 右端を進めていく
    while right < n and total < k:
        total += a[right]
        right += 1
    if total < k:
        break
    else:
        ans += n - right + 1
    if right == left:
        right += 1
    else:
        total -= a[left]
print(ans)
