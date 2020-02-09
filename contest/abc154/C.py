n = int(input())
a = list(map(int, input().split()))
now = set()
for i in a:
    now.add(i)
if len(now) == n:
    print('YES')
else:
    print('NO')
