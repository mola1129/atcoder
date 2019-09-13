n = int(input())
a = list(map(int, input().split()))
a.sort()
i = a[0]
j = a[1]
while 1:
    max_num = max(i, j)
    min_num = min(i, j)
    max_num -= min_num
