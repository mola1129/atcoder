n, m, x = map(int, input().split())
a = list(map(int, input().split()))
cost = [0] * (n - 1)
for i in a:
    cost[i - 1] = 1
print(min(sum(cost[0:x - 1]), sum(cost[x:n - 1])))
