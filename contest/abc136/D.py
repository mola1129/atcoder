s = input()
switch = []
ans = [0] * (len(s))
# R→L or L→Rの変化部分を保存
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        switch.append(i + 1)

# switch[i]: iが偶数なら　R→L
#            iが奇数なら　L→Rの境目番号
start = 0
for i in range(0, len(switch), 2):
    # for文終了時のエラー処理
    if i == len(switch) - 1:
        end = len(s)
    else:
        end = switch[i + 1]
    #  ...RL...LR部分においてカウントする
    for num in range(start, end):
        # 境目部分の偶奇と一致すれば、最終的にその場所に位置する
        if num % 2 == switch[i] % 2:
            ans[switch[i]] += 1
        else:
            ans[switch[i] - 1] += 1
    start = end
print(*ans)
