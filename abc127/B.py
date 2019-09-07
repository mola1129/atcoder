r,D,x = map(int,input().split())
X = []
X.append(x)

for i in range(1,11):
    result = r*X[i-1]-D
    X.append(result)

for i in range(1,11):
    print(X[i])
