n = int(input())
s = input()
ans = 0
for i in range(1, n - 1):
    cnt = 0
    left = set(s[:i])
    right = set(s[i:])
    for alphabet in left:
        if alphabet in right:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
