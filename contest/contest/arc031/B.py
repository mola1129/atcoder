import copy
world = [list(input()) for _ in range(10)]
# 移動は4方向
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 繋がっている島1つを"x"で塗りつぶす
def dfs(x, y):
    world2[x][y] = "x"
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx and nx < 10 and 0 <= ny and ny < 10 and world2[nx][ny] == "o":
            dfs(nx, ny)


# 1マスを"o"に上書きして、dfsを実行
for i in range(10):
    for j in range(10):
        world2 = copy.deepcopy(world)
        world2[i][j] = "o"
        dfs(i, j)
        cnt = 0
        for k in range(10):
            if "".join(world2[k]) == "xxxxxxxxxx":
                cnt += 1
        # 10✕10マス分一つも"o"が残っていなければOK
        if cnt / 10 == 1:
            print("YES")
            exit()
print("NO")
