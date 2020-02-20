from operator import itemgetter
n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs = sorted(jobs, key=itemgetter(1))
total = 0
for a, b in jobs:
    total += a
    if total > b:
        print('No')
        exit()
print('Yes')
