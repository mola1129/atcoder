n = list(input())
ans = 0
if len(n[1:]) == n[1:].count('9'):
    ans = sum(list(map(int, n)))
else:
    ans = int(n[0]) - 1 + 9 * (len(n) - 1)
print(ans)
