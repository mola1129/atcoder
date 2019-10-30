n = int(input())
a = list(map(int, input().split()))
cost = [float('inf')] * n
cost[0] = 0
cost[1] = abs(a[0] - a[1])
for i in range(2, n):
    cost[i] = min(cost[i - 1] + abs(a[i] - a[i - 1]),
                  cost[i - 2] + abs(a[i] - a[i - 2]))
print(cost[n - 1])
