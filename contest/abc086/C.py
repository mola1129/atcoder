n = int(input())
plan = [tuple(map(int, input().split())) for _ in range(n)]
plan.insert(0, (0, 0, 0))
for i in range(1, n + 1):
    time_limit = plan[i][0] - plan[i - 1][0]
    distance = abs(plan[i][1] - plan[i - 1][1]) + \
        abs(plan[i][2] - plan[i - 1][2])
    if time_limit < distance or (time_limit % 2 != distance % 2):
        print('No')
        exit()
print('Yes')
