n = int(input())
a = list(map(int, input().split()))
x = [0] * n
# 合計を求める
x[0] = sum(a)
# 初項x_1
for i in range(1, n - 1, 2):
    x[0] -= 2 * a[i]
# 漸化式で前から求める
for i in range(1, n):
    x[i] = 2 * a[i - 1] - x[i - 1]
print(*x)
