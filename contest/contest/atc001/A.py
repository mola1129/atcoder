# 再帰呼び出しの上限を設定
import sys
sys.setrecursionlimit(10 ** 9)

h, w = map(int, input().split())
# stringはリストに帰ることで修正可能
c = [list(input()) for _ in range(h)]
# 移動先の4方向
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
ans = "No"


# goalに到達可能ならansを"Yes"にする関数
def reach_goal(start):
    for i in range(4):
        # スタートを壁に書き換える
        c[start[0]][start[1]] = "#"
        # (x,y): 移動先座標
        x = start[0] + move[i][0]
        y = start[1] + move[i][1]
        # 範囲を超えていないか確認
        if 0 <= x and x < h and 0 <= y and y < w:
            # 道なら処理を続ける
            if c[x][y] == ".":
                reach_goal((x, y))
            # ゴールに到着したら"Yes"
            elif c[x][y] == "g":
                global ans
                ans = "Yes"


# スタート地点を見つける
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            reach_goal((i, j))
            break
print(ans)
