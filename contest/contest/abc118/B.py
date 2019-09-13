n, m = map(int, input().split())
cnt = [0] * m
for _ in range(n):
    k = list(map(int, input().split()))
    for i in range(1, len(k)):
        cnt[k[i]-1] += 1
print(cnt.count(n))
