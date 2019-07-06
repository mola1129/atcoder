N,K = map(int, input().split())
cnt = 0
while 2**cnt < K:
    cnt += 1
result = ((1/2)**cnt)/N
for i in range(2,N+1):
    while (2**cnt)+(2**cnt)*(i-1) >= K and cnt >= 0:
        cnt -= 1
    if cnt == -1:
        result += (N-i+1)/N
        break
    cnt += 1
    result += ((1/2)**cnt)/N
print(result)
