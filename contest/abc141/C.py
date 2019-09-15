n, k, q = map(int, input().split())
correct = [0] * n
# 正解数をカウント
for _ in range(q):
    a = int(input())
    a -= 1
    correct[a] += 1
# (問題数) - (正解数) = (下がる点数)
# これがkより大きければ良い
for i in range(n):
    if (q - correct[i]) < k:
        print("Yes")
    else:
        print("No")
