n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
ans = 0
for i in range(n):
    candy = sum(a[0][:i + 1]) + sum(a[1][i:])
    ans = max(ans, candy)
print(ans)
