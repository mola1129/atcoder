import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
# 深さ優先探索で各直線を考える


def main():
    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            # 累積和の計算
            ans[u] += ans[v]
            dfs(u, v)

    n, q = map(int, input().split())
    # tree[i]: 頂点i+1の子どもたち
    tree = [[] for i in range(n)]
    ans = [0] * n

    for _ in range(0, n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    for _ in range(q):
        p, x = map(int, input().split())
        ans[p - 1] += x

    # 根ノードの頂点 1 から開始
    dfs(0, -1)

    print(*ans)


if __name__ == '__main__':
    main()
