N,M = map(int,input().split())

l_max = 1
r_min = N
for i in range(0,M):
    l,r = map(int,input().split())
    if l_max < l:
        l_max = l
    if r_min > r:
        r_min = r

if l_max > r_min:
    print(0)
else:
    print(r_min-l_max+1)
