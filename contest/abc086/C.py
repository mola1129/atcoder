n = int(input())
prev_dst = prev_t = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    dst = x + y
    ddst = abs(dst - prev_dst)
    dt = t - prev_t
    if t % 2 != dst % 2 or ddst > dt:
        print('No')
        exit()
    prev_t, prev_dst = t, dst
print('Yes')
