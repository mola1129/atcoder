n, k, s = map(int, input().split())
ans = []
for i in range(k):
    ans.append(s)
for i in range(n - k):
    if s + 1 <= 10 ** 9:
        ans.append(s + 1)
    else:
        ans.append(1)
print(*ans)
