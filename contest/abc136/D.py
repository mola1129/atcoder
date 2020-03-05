s = input()
n = len(s)
ans = [0] * n
# 偶奇のカウント
cnt_even = 0
cnt_odd = 0
# 'RL'が見つかったときの'R'の要素番号
index = 0
for i in range(n - 1):
    if s[i] == 'R' and s[i + 1] == 'L':
        index = i
    if i % 2:
        cnt_odd += 1
    else:
        cnt_even += 1
    # 'LR'部が境界
    if s[i] == 'L' and s[i + 1] == 'R' or i == n - 2:
        # 要素右端のコーナーケース
        if i == n - 2:
            if (i + 1) % 2:
                cnt_odd += 1
            else:
                cnt_even += 1
        if index % 2:
            ans[index] += cnt_odd
            ans[index + 1] += cnt_even
        else:
            ans[index] += cnt_even
            ans[index + 1] += cnt_odd
        cnt_even = 0
        cnt_odd = 0
print(*ans, sep=' ')
