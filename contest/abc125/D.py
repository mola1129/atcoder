n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if a[i] < 0:
        cnt += 1
        a[i] *= -1
a.sort()
cnt %= 2
print(sum(a) - 2 * sum(a[:cnt]))
