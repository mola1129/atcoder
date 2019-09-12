d, g = map(int, input().split())
# (問題数,ボーナス)のタプルで保存
p = [tuple(map(int, input().split())) for _ in range(d)]
ans = 1000
#  全完する問題の組み合わせを考える
for i in range(2 ** d):
    cnt = 0
    total = 0
    for j in range(d):
        # 全完する場合
        if (i >> j) & 1:
            # 問題数と得点＆ボーナスを追加
            cnt += p[j][0]
            total += (j + 1) * 100 * p[j][0] + p[j][1]
    #  まだ目標に届かない場合
    if total < g:
        # 得点の高い問題から取り掛かるのか最適
        for j in range(d - 1, -1, -1):
            # 全完しない予定だった問題を考慮する
            if (i >> j) & 1:
                continue
            for k in range(p[j][0]):
                if total >= g:
                    break
                # 得点と問題数を追加
                total += 100 * (j + 1)
                cnt += 1
    # 最小のものを求める
    ans = min(ans, cnt)
print(ans)
