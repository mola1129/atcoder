n = int(input())
s = [input() for _ in range(n)]
prefix = ['M', 'A', 'R', 'C', 'H']
cnt = [0] * 5
ans = 0
for i in range(n):
    for j in range(5):
        if s[i][0] == prefix[j]:
            cnt[j] += 1
for i in range(2 ** 5):
    flag = [False] * 5
    for j in range(5):
        if (i >> j) & 1:
            flag[j] = True
    if flag.count(True) == 3:
        tmp = 1
        for k in range(5):
            if flag[k]:
                tmp *= cnt[k]
        ans += tmp
print(ans)
