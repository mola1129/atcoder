n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
strength = [0] * (n + 1)
for i in range(1, n):
    strength[i] = strength[i - 1] + a[i - 1]
for i in range(len(a) - 1, -1, -1):
    if strength[i] * 2 < a[i]:
        break
    ans += 1
print(ans)
