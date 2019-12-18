import collections
n = int(input())
a = list(map(int, input().split()))
b = collections.deque([])
flag = False
if n % 2 == 1:
    flag = True
for i in range(n):
    if flag:
        b.appendleft(a[i])
        flag = False
    else:
        b.append(a[i])
        flag = True
print(*b)
