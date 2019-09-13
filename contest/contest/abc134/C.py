n = int(input())
a = []
for i in range(0, n):
    a.append((int(input()), i))
a.sort()
a.reverse()
for i in range(0, n):
    num = 0
    while a[num][1] == i:
        num += 1
    print(a[num][0])
