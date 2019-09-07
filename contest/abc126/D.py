from collections import deque


def main():
    # 幅優先探索
    def bfs():
        q = deque([0])
        while q:
            u = q.popleft()
            # 接続頂点を精査
            for v, w in g[u]:
                # まだチェックしていない頂点をチェック
                if color[v] == -1:
                    q.append(v)
                    # 偶数なら同じ色で塗る
                    if w == 0:
                        color[v] = color[u]
                    else:
                        color[v] = color[u] ^ 1

    n = int(input())
    g = [[] for _ in range(n)]
    # 塗りつぶし結果
    color = [-1] * n
    # スタートは黒で塗っておく
    color[0] = 1
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        w %= 2
        g[u].append((v, w))
        g[v].append((u, w))
    bfs()
    print(*color)


if __name__ == "__main__":
    main()
