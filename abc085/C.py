n, y = map(int, input().split())
# i,jの範囲に注意
for i in range(n + 1):
    for j in range(n - i + 1):
        if 10000 * i + 5000 * j + 1000 * (n - i - j) == y:
            # 見つかったら処理を終了
            print(i, j, n - i - j)
            exit()
# 見つからなければ-1を返す
print(-1, -1, -1)
