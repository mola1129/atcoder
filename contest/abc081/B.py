n = int(input())
a = list(map(int, input().split()))
cnt = 0
flag = False
for i in range(10000):
    for j in range(n):
        if a[j] % 2 != 0:
            flag = True
        a[j] /= 2
    if flag:
        break
    cnt += 1
print(cnt)
