n = int(input())
a = list(map(int, input().split()))
cost = [0] * (n + 1)
for i in range(1, n + 1):
    cost[i] = cost[i - 1]
    cost[i] += a[i - 1]
ans = float('inf')
for i in range(1, n):
    ans = min(ans, abs(cost[i] - cost[n] + cost[i]))
print(ans)
