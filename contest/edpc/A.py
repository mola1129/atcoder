n = int(input())
h = list(map(int, input().split()))
cost = [float('inf')] * n
cost[1] = abs(h[0] - h[1])
for i in range(2, n):
    one = cost[i - 1] + abs(h[i - 1] - h[i])
    two = cost[i - 2] + abs(h[i - 2] - h[i])
    cost[i] = min(one, two)
print(cost[n - 1])
