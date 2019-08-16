from collections import deque


# 幅優先探索
def bfs(sx, sy, gx, gy):
    q = deque([(sx, sy)])
    # その地点に到達するまでに壁を壊した回数
    destroy[sx][sy] = 0
    while q:
        x, y = q.popleft()
        # 4近傍の調査
        for dx, dy in nb:
            nx = x + dx
            ny = y + dy
            # まだチェックしていない and 範囲内のマスか確認
            if 0 <= nx and nx < h and 0 <= ny and ny < w and destroy[nx][ny] == -1:
                # 壁なら破壊コストを1増加
                if maze[nx][ny] == "#":
                    destroy[nx][ny] = destroy[x][y] + 1
                    q.append((nx, ny))
                # 道なら破壊コストはそのまま
                else:
                    destroy[nx][ny] = destroy[x][y]
                    # 見つかった道は優先的に処理
                    q.appendleft((nx, ny))

    # 破壊コストが2回以下ならYES
    if destroy[gx][gy] <= 2:
        return "YES"
    else:
        return "NO"


h, w = map(int, input().split())
maze = [input() for _ in range(h)]
destroy = [[-1] * w for _ in range(h)]
nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
sx = 0
sy = 0
gx = 0
gy = 0
# スタートとゴールの位置を調査
for i in range(h):
    for j in range(w):
        if maze[i][j] == "s":
            sx = i
            sy = j
        if maze[i][j] == "g":
            gx = i
            gy = j

print(bfs(sx, sy, gx, gy))
