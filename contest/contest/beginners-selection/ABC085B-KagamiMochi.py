N = int(input())
d = []
for i in range(0,N):
    d.append(int(input()))

d.sort()

cnt = 1
for i in range(0,N-1):
    if d[i] < d[i+1]:
        cnt += 1

print(cnt)
