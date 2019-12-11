a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    num = str(i)
    n = len(num)
    for j in range(n // 2):
        if num[j] != num[n - 1 - j]:
            break
        elif j == n // 2 - 1:
            ans += 1
print(ans)
