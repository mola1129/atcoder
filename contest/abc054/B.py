n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
flag = False
for i in range(n):
    for j in range(n):
        for k in range(m):
            for l in range(m):
                if i + k >= n or j + l >= n:
                    flag = True
                    break
                if a[i + k][j + l] != b[k][l]:
                    flag = True
                    break
            if flag:
                flag = False
                break
            if k == m - 1:
                print('Yes')
                exit()
print('No')
