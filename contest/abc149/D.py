n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ans = 0
for j in range(k):
    pre = 'no'
    for i in range(n - 1 - j, -1, -k):
        score = 0
        if t[i] == 'r' and pre != 'p':
            score = p
            pre = 'p'
        if t[i] == 's' and pre != 'r':
            score = r
            pre = 'r'
        if t[i] == 'p' and pre != 's':
            score = s
            pre = 's'
        if score == 0:
            pre = 'no'
        ans += score
print(ans)
