import itertools
n, m = map(int, input().split())
# (x,y) でリストに保存
xy = [tuple(map(int, input().split())) for _ in range(m)]
ans = 1
for i in range(2, n + 1):
    # 冪集合もどきを作成
    for c in itertools.combinations(range(1, n + 1), i):
        # 必要な関係が存在しているかのフラグ
        exist = 1
        for j in range(i - 1):
            for k in range(j + 1, i):
                # 一つでも関係が存在しなければ派閥構築不可
                if not ((c[j], c[k]) in xy):
                    exist = 0
                    break
        if exist == 1:
            ans = i
print(ans)
