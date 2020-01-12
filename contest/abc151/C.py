n, m = map(int, input().split())
ac = [False] * n
cnt = [0] * n
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if s == "AC" and not ac[p - 1]:
        ac[p - 1] = True
    if s == "WA" and not ac[p - 1]:
        cnt[p - 1] += 1
ans_ac = 0
ans_wa = 0
for i in range(n):
    if ac[i]:
        ans_ac += 1
        ans_wa += cnt[i]
print(ans_ac, ans_wa)
