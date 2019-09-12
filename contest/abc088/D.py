from collections import deque


# 幅優先探索
def bfs(sx, sy, gx, gy):
    # スタート地点を設定
    q = deque([(sx, sy)])
    # コスト1とする(通過するマス目を数えるため)
    cost[sx][sy] = 1
    while q:
        x, y = q.popleft()
        # 4近傍を調査
        for dx, dy in nb:
            nx = x + dx
            ny = y + dy
            # 通過可能条件の判定
            if 0 <= nx and nx < h and 0 <= ny and ny < w and grid[nx][ny] == "." and cost[nx][ny] == float("inf"):
                # キューに追加
                q.append((nx, ny))
                cost[nx][ny] = cost[x][y] + 1
                # ゴールなら終了
                if nx == gx and ny == gy:
                    return cost[nx][ny]
    # ゴール到達不可
    return -1


h, w = map(int, input().split())
# マス目
grid = [list(input()) for _ in range(h)]
# そのマスに到達するために掛かるコスト
cost = [[float("inf")] * w for _ in range(h)]
# 4近傍の移動
nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]
black_cnt = 0
ans = 0


# 黒マスの総数を求める
for i in range(h):
    black_cnt += str(grid[i]).count("#")

can_reach = bfs(0, 0, h - 1, w - 1)

if can_reach > 0:
    # 全てのマス数 - 通過するマス数(スタートとゴールを含む) = (黒で塗っても良い不要なマスの数)
    # (黒で塗っても良い不要なマスの数) - (元の黒マスの数) = (得点)
    print(h * w - can_reach - black_cnt)
else:
    # ゴール到達不可は-1を返す
    print(can_reach)
