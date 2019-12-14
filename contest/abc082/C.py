n = int(input())
a = list(map(int, input().split()))
a.sort()
a.append(0)
num = a[0]
cnt = 1
ans = 0
for i in range(1, n + 1):
    if a[i] == num:
        cnt += 1
    else:
        diff = num - cnt
        if diff <= 0:
            ans += abs(diff)
        else:
            ans += cnt
        num = a[i]
        cnt = 1
print(ans)
