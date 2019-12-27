n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = float('inf')
index = float('inf')
for i in range(n - 1):
    now = abs(a[-1] / 2 - a[i])
    if ans > now:
        ans = now
        index = i
print(a[-1], a[index])
