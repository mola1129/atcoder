n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = x
for i in range(n):
    for j in range(1, d + 1, a[i]):
        ans += 1
print(ans)
