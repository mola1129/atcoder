import math
N, K = map(int, input().split())
a = list(map(int, input().split()))
# 必ず1を含めて操作する
# 1回目はK個置き換わる
N -= K
# 2回目以降はK-1個
print(math.ceil(N / (K - 1)) + 1)
