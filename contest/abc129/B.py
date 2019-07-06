n = int(input())
w = list(map(int, input().split()))
result = 100000
for t in range(1,n):
    total1 = 0
    total2 = 0
    for i in range(0,t):
        total1 += w[i]
    for i in range(t,n):
        total2 += w[i]
    result = min(result,abs(total1-total2))

print(result)
