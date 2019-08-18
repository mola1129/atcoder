def dfs(now, prev):
    # 閉路の有無のフラグ
    global is_closed
    for next in g[now]:
        # u → v → u の場合のときの対策
        if next != prev:
            if visited[next]:
                is_closed = True
            else:
                visited[next] = True
                dfs(next, now)


n, m = map(int, input().split())
# g[i]: 頂点 i+1 と辺で繋がっている頂点の集合
g = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)


ans = 0
for i in range(n):
    is_closed = False
    # まだ訪ねていない場所から開始
    if not visited[i]:
        dfs(i, -1)
        # 閉路の場合はカウントしない
        if not is_closed:
            ans += 1

print(ans)
