def main():
    import collections
    import sys
    input = sys.stdin.readline
    n = int(input())
    d = list(map(int, input().split()))
    # 各距離の頂点数を求める
    c = collections.Counter(d)
    ans = 1
    tmp = -1
    # 頂点1のみが0である必要がある
    if d[0] != 0 or c[0] > 1:
        print(0)
        exit()
    # 個数の計算
    for i in range(2, n):
        if i - 1 in c.keys():
            ans *= c[i - 1] ** c[i]
            ans %= 998244353
        else:
            tmp = i
            break
    # 距離が連番になっていなければ到達不可能
    if tmp >= 0:
        for j in range(tmp, n):
            if j in c.keys():
                print(0)
                exit()
    print(ans)


if __name__ == "__main__":
    main()
