import math
n, d = map(int, input().split())
watch = d * 2 + 1
if n < d:
    print(1)
else:
    print(math.ceil(n/watch))
