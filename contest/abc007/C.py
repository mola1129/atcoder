# キューを利用
from collections import deque


# 幅優先探索
def bfs():
    # スタートの設定
    q = deque([(sx, sy)])
    cost[sy][sx] = 0
    while q != []:
        # 次に処理する地点を取り出す
        x, y = q.popleft()
        # 4近傍を調査
        for dx, dy in nb:
            nx = x + dx
            ny = y + dy
            # 進める場所であるか・初めて訪ねる場所であるか確認
            if 0 <= nx and nx < c and 0 <= ny and ny < r and maze[ny][nx] == "." and cost[ny][nx] == 300:
                # キューに追加
                q.append((nx, ny))
                # コストを設定
                cost[ny][nx] = cost[y][x] + 1
                # ゴールが見つかればそのコストを返す
                if nx == gx and ny == gy:
                    return cost[gy][gx]


r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy, sx, gy, gx = sy - 1, sx - 1, gy - 1, gx - 1

maze = [input() for _ in range(r)]
cost = [[300] * c for _ in range(r)]
# 4近傍への移動4パターン
nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]

print(bfs())
