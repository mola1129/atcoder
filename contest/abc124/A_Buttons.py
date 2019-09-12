a,b = map(int, input().split())
c = 0

for i in range(0,2):
    if a > b:
        c += a
        a -= 1
    else:
        c += b
        b -= 1

print(c)
