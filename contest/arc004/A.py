import math


# 2点間の距離を求める
def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d


n = int(input())
# タプル(x,y)で保存
xy = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n-1):
    for j in range(i + 1, n):
        # 最大の長さを保持
        dst = get_distance(xy[i][0], xy[i][1], xy[j][0], xy[j][1])
        ans = max(ans, dst)
print(ans)
