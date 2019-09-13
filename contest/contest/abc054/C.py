import itertools
n, m = map(int, input().split())
# 頂点の接続
e = [[] for _ in range(n)]
ans = 0

# e[u]: u → v への辺が存在
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    e[u].append(v)
    e[v].append(u)

# 順列を生成
for route in itertools.permutations(range(1, n), n - 1):
    # すでに訪れているかのフラグ
    visited = [False] * n
    # スタートは訪問済みとする
    visited[0] = True
    route = list(route)
    # スタートは必ず頂点1
    route.insert(0, 0)
    for i in range(1, n):
        now = route[i - 1]
        nxt = route[i]
        # 訪ねていないかつ、繋がっているならOK
        if str(nxt) in str(e[now]) and not(visited[nxt]):
            visited[nxt] = True
            # 全部OKなら加算する
            if i == n - 1:
                ans += 1
        else:
            break

print(ans)
