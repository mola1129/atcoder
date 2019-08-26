N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
for z in range(-100, 101):
    if X < z and z <= Y and x[N - 1] < z and z <= y[0]:
        print("No War")
        exit()
print("War")
