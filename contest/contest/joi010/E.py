from collections import deque


# 幅優先探索
def bfs():
    # そのマスに到達するためのコスト
    cost = [[float("inf")] * w for _ in range(h)]
    # スタート地点を設定
    q = deque([(sx, sy)])
    cost[sy][sx] = 0
    while q != []:
        x, y = q.popleft()
        # 4近傍を調査
        for dx, dy in nb:
            nx = x + dx
            ny = y + dy
            # 訪ねたことが無い・通れるマスならキューに追加
            if 0 <= nx and nx < w and 0 <= ny and ny < h and maze[ny][nx] != "X" and cost[ny][nx] == float("inf"):
                q.append((nx, ny))
                cost[ny][nx] = cost[y][x] + 1
                # ゴールなら終了
                if nx == gx and ny == gy:
                    return cost[gy][gx]


h, w, n = map(int, input().split())
# 迷路
maze = [input() for _ in range(h)]
# 4近傍への移動
nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
# 各チーズ座標
cheese = []
ans = 0
# スタート座標を把握
for row in range(h):
    column = str(maze[row]).find("S")
    if column != -1:
        cheese.append((column, row))
        break
# チーズ座標を把握
for i in range(1, n + 1):
    for row in range(h):
        column = str(maze[row]).find(str(i))
        if column != -1:
            cheese.append((column, row))
            break

# 各チーズ間の最短距離の総和を求める
for i in range(n):
    sx = cheese[i][0]
    sy = cheese[i][1]
    gx = cheese[i + 1][0]
    gy = cheese[i + 1][1]
    ans += bfs()
print(ans)
