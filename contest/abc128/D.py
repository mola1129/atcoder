from collections import deque
from copy import deepcopy
n, k = map(int, input().split())
v = deque(map(int, input().split()))
# 取り出せる最大回数
t = min(n, k)
ans = 0
# A,Bの操作の回数で全探索
for a in range(t + 1):
    for b in range(t + 1 - a):
        # 初期化
        vv = deepcopy(v)
        # 今持っている宝石たち
        belongings = []
        # 取り出していく
        for _ in range(a):
            if vv:
                jewelry = vv.popleft()
                belongings.append(jewelry)
        for _ in range(b):
            if vv:
                jewelry = vv.pop()
                belongings.append(jewelry)
        # ソートして、負の宝石は可能な限り筒に戻す
        belongings.sort()
        for i in range(a + b):
            if belongings[i] < 0 and i < (k - a - b):
                belongings[i] = 0
        ans = max(sum(belongings), ans)
print(ans)
