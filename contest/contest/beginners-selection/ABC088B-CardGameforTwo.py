N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0

a.sort()
a.reverse()
for i in range(0,N,2):
    Alice += a[i]
for j in range(1,N,2):
    Bob += a[j]

print(Alice-Bob)
