n = int(input())
v = list(map(int, input().split()))
while len(v) != 1:
    v.sort()
    v.append((v.pop(0) + v.pop(0)) / 2)
print(v[0])
