N,Y = map(int, input().split())
result = [-1]*3

for i in range(0,N+1):
    j = (-N + i + Y // 1000 - 10*i) // 4
    k = N - i - j
    if 10000*i + 5000*j + 1000*k == Y and i >= 0 and j >= 0 and k >= 0:
        result[0] = i
        result[1] = j
        result[2] = k
        break;
for num in result:
    print(num ,end=" ")
