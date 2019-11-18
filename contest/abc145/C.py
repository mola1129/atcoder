import itertools
import math
n = int(input())
town = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
cnt = 0

for p in itertools.permutations(range(0, n), n):
    for i in range(n - 1):
        distance = (town[p[i]][0] - town[p[i + 1]][0]) ** 2 + \
            (town[p[i]][1] - town[p[i + 1]][1]) ** 2
        ans += math.sqrt(distance)
    cnt += 1
ans /= cnt
print(ans)
