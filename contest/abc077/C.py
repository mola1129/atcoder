import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
c.sort()
ans = 0
for i in range(n):
    lower_cnt = bisect.bisect_left(a, b[i])
    upper_cnt = len(b) - bisect.bisect_right(c, b[i])
    ans += lower_cnt * upper_cnt
print(ans)
