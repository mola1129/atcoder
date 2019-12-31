import math
n = int(input())
a = list(map(int, input().split()))
average = sum(a) / n
if average % 1 >= 0.5:
    average = math.ceil(average)
else:
    average = math.floor(average)
ans = 0
for i in range(n):
    ans += (average - a[i]) ** 2
print(ans)
