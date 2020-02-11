n, m = map(int, input().split())
student = [tuple(map(int, input().split())) for _ in range(n)]
check_points = [tuple(map(int, input().split())) for _ in range(m)]
for a, b in student:
    dst_min = float('inf')
    ans = float('inf')
    for i, (c, d) in enumerate(check_points):
        now = abs(a - c) + abs(b - d)
        if now < dst_min:
            dst_min = now
            ans = i + 1
    print(ans)
