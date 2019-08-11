import heapq
n, m = map(int, input().split())
jobs = [tuple(map(int, input().split())) for i in range(n)]
# 必要な日数の照準にソートする
jobs.sort()
# 次に選ぶバイト候補の保存場所
money = []
ans = 0

i = 0
# より制約の強い、最終リミットに近い日に行うバイトの割当てから攻めていく
for limit in range(1, m + 1):
    # limit日までに報酬のもらえるアルバイトを抽出
    while i < n and jobs[i][0] <= limit:
        a = jobs[i][0]
        b = jobs[i][1]
        # 次に選ぶバイト候補に追加
        heapq.heappush(money, -b)
        i += 1
    # 要素数が空の場合のエラー処理
    if money != []:
        ans -= heapq.heappop(money)

print(ans)
