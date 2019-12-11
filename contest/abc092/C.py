n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)
distance = [0] * (n + 1)
total = 0
for i in range(1, n + 2):
    distance[i - 1] = a[i] - a[i - 1]
    total += abs(a[i] - a[i - 1])
for i in range(1, n + 1):
    diff = abs(distance[i]) + abs(distance[i - 1]) - \
        abs(distance[i] + distance[i - 1])
    print(total - diff)
