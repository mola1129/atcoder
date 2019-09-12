import copy
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.append(0)
tmp = copy.copy(b)
ans = 0
for i in range(0, n):
    ans += min(a[i], b[i])
    b[i + 1] += min(max(b[i] - a[i], 0), tmp[i])
ans += min(a[n], b[n])
print(ans)
