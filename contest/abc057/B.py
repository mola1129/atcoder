n, m = map(int, input().split())
student = [tuple(map(int, input().split())) for _ in range(n)]
check_points = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(n):
    distance = float('inf')
    index = float('inf')
    for j in range(m):
        now = abs(student[i][0] - check_points[j][0]) + \
            abs(student[i][1] - check_points[j][1])
        if now < distance:
            distance = now
            index = j + 1
    print(index)
