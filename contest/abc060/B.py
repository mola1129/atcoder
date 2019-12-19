a, b, c = map(int, input().split())
rest = set([])
for i in range(a, (b + 1) * a, a):
    rest.add(i % b)
if c in rest:
    print('YES')
else:
    print('NO')
