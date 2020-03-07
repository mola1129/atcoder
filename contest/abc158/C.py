a, b = map(int, input().split())
for i in range(10, 1100):
    nowA = int(0.08 * i)
    nowB = int(0.1 * i)
    if nowA == a and nowB == b:
        print(i)
        exit()
print(-1)
