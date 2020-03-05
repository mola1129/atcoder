n = int(input())
a = list(map(int, input().split()))
b = [0] * (n + 1)
# 後ろからボールの有無を決定
for i in range(n, 0, -1):
    cnt = sum(b[::i])
    # 条件と異なるならボールを投入
    if cnt % 2 != a[i - 1]:
        b[i] = 1
m = sum(b)
print(m)
for i in range(1, n + 1):
    if b[i]:
        print(i, end=' ')
