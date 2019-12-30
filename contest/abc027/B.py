n = int(input())
a = list(map(int, input().split()))
total = sum(a)
if total % n != 0:
    print(-1)
    exit()
num = total // n
ans = 0
for i in range(n - 1):
    left = sum(a[:i + 1])
    right = sum(a[i + 1:])
    if left < num * (i + 1) or right < num * (n - i - 1):
        ans += 1
print(ans)
