a, b, t = map(int, input().split())
for ans in range(b, 6000, b - a):
    if ans >= t:
        print(ans)
        exit()
print(-1)
