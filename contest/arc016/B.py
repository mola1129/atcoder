n = int(input())
x = [input() for _ in range(n)]
ans = 0
for j in range(9):
    flag = False
    for i in range(n):
        if x[i][j] == 'o':
            flag = True
        elif flag:
            ans += 1
            flag = False
        if x[i][j] == 'x':
            ans += 1
        if i == n - 1 and flag:
            ans += 1
print(ans)
