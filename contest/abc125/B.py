N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
diff = []
for i in range(N):
    diff.append(V[i]-C[i])
sum = 0
for i in range(N):
    if diff[i] > 0:
        sum += diff[i]
print(sum)
