n = int(input())
ans = 0
cnt = [[0] * 9 for _ in range(9)]
for i in range(1, n + 1):
    one = str(i)
    if one[-1] == '0':
        continue
    cnt[int(one[0]) - 1][int(one[-1]) - 1] += 1
for i in range(9):
    for j in range(9):
        ans += cnt[i][j] * cnt[j][i]
print(ans)
