n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
for i in range(n):
    h[i] = abs(a - (t - h[i] * 0.006))
tmp = float("inf")
ans = float("inf")
for i in range(n):
    if tmp > h[i]:
        tmp = h[i]
        ans = i + 1
print(ans)
