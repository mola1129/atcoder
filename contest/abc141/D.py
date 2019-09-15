# プライオリティキューの利用
import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
# 最大の値段を取り出すために、全て(-1)を掛ける
a = list(map(lambda x: x * (-1), a))
heapq.heapify(a)
# 割引券を使い切るまで行う
while m != 0:
    # 最大の値段を取り出す
    price = heapq.heappop(a) * (-1)
    # 割引
    price //= 2
    m -= 1
    # プライオリティキューへ戻す
    heapq.heappush(a, (-1) * price)
# 最初に(-1)掛けているので、符号を戻す
print(sum(a) * (-1))
