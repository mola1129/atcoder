n, m = map(int, input().split())
g = [[False] * n for _ in range(n)]
visited = [False] * n
a = []
b = []
ans = 0


def dfs(v):
    visited[v] = True
    for to in range(n):
        if not g[v][to]:
            continue
        if visited[to]:
            continue
        dfs(to)


for _ in range(m):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    a.append(ai)
    b.append(bi)
    g[ai][bi] = True
    g[bi][ai] = True

for i in range(m):
    # 辺を一つ消す
    g[a[i]][b[i]] = False
    g[b[i]][a[i]] = False
    # 訪問済みリストの初期化
    for j in range(n):
        visited[j] = False
    dfs(0)
    # 連結性の判定
    for j in range(n):
        if not visited[j]:
            ans += 1
            break
    # 消した辺を元に戻す
    g[a[i]][b[i]] = True
    g[b[i]][a[i]] = True
print(ans)
