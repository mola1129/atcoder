from collections import deque
n, x = map(int, input().split())
a = list(map(int, input().split()))
lost_index = deque()
res = 0
for i in range(n):
    if a[i] > 0:
        res ^= a[i]
    else:
        lost_index.append(i)
tmp = res ^ x
if 0 <= tmp and tmp <= x and lost_index:
    i = lost_index.popleft()
    a[i] = tmp
    while lost_index:
        i = lost_index.popleft()
        a[i] = 0
    print(*a)
elif 0 <= tmp - x and tmp - x <= x and len(lost_index) > 1:
    i = lost_index.popleft()
    a[i] = x
    i = lost_index.popleft()
    a[i] = tmp - x
    while lost_index:
        i = lost_index.popleft()
        a[i] = 0
    print(*a)
else:
    print(-1)
