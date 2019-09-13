n = int(input())
b = list(map(int, input().split()))
ans = [0] * n
ans[0] = b[0]
ans[1] = b[0]
for i in range(1, n - 1):
    ans[i] = min(ans[i], b[i])
    ans[i + 1] = b[i]
print(sum(ans))
