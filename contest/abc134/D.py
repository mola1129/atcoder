n = int(input())
a = list(map(int, input().split()))
ball = [0] * n
# 後ろからボールの有無を決定
for i in range(n, 0, -1):
    cnt = 0
    # 倍数のボール有無をチェック
    for j in range(i * 2, n + 1, i):
        cnt += ball[j-1]
    cnt %= 2
    # 条件と異なるならボールを投入
    if cnt != a[i - 1]:
        ball[i - 1] = 1
# ボールの入っている箱の個数
print(ball.count(1))
# ボールの入った箱のインデックスを出力
for i in range(0, n):
    if ball[i] == 1:
        print(i+1, end=" ")
