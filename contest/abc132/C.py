import math
N = int(input())
d = list(map(int, input().split()))
d.sort()
num = N//2-1
print(d[num+1]-d[num])
