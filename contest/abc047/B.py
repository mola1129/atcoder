w, h, n = map(int, input().split())
min_xy = [0, 0]
max_xy = [w, h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        min_xy[0] = max(min_xy[0], x)
    if a == 2:
        max_xy[0] = min(max_xy[0], x)
    if a == 3:
        min_xy[1] = max(min_xy[1], y)
    if a == 4:
        max_xy[1] = min(max_xy[1], y)
if max_xy[0] >= min_xy[0] and max_xy[1] >= min_xy[1]:
    print((max_xy[0] - min_xy[0]) * (max_xy[1] - min_xy[1]))
else:
    print(0)
