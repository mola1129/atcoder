h, a = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
if total >= h:
    print('Yes')
else:
    print('No')
