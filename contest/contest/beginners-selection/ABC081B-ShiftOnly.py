n = int(input())
a = list(map(int, input().split()))
cnt = 0
i = 0
while a[i] % 2 == 0:
    a[i] /= 2
    i += 1
    if i == n-1:
        i = 0
        cnt += 1

print(cnt)
