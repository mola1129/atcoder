from operator import itemgetter
N = int(input())
sp = []
for i in range(0,N):
    s,p = input().split()
    p = int(p)
    sp.append((s,p,i+1))

sp.sort(key=itemgetter(1), reverse=True)
sp.sort(key=itemgetter(0))

for s,p,i in sp:
    print(i, end=" ")
