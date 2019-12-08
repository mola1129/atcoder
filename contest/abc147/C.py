N = int(input())
a = [[] for i in range(N)]
ans = 0
for i in range(N):
    times = int(input())
    for j in range(times):
        a[i].append(tuple(map(int, input().split())))

for i in range(2 ** N):
    flag2 = False
    cnt = 0
    flag = [0] * N
    for j in range(N):
        if (i >> j) & 1:
            flag[j] = 1
    for k in range(N):
        if flag[k] == 1:
            for m in range(len(a[k])):
                x, y = a[k][m]
                if flag[x - 1] != y:
                    flag2 = True
                    break
        if flag2:
            break
        if k == N - 1:
            cnt = flag.count(1)

    ans = max(ans, cnt)
print(ans)
