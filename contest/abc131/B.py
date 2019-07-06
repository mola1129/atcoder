N,L = map(int, input().split())
list = []
sum = 0
min = 10000
sign = 1
for i in range(1,N+1):
    sum += L+i-1
    list.append(L+i-1)
for num in list:
    if min > abs(num):
        min = abs(num)
        if num > 0:
            sign = 1
        else:
            sign = -1
print(sum-min*sign)
