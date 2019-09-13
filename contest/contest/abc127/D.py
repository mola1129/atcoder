N,M = map(int,input().split())
A = list(map(int,input().split()))
cards = []
for i in range(0,N):
    cards.append((A[i],1))

for i in range(0,M):
    b,c = map(int,input().split())
    cards.append((c,b))

cards.sort()
cards.reverse()

result = 0
total = N
for num, cnt in cards:
    total -= cnt
    result += num*cnt
    if total < 0:
        result += num * total
        break
print(result)
