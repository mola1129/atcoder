a, b, c = map(int, input().split())
if c - a - b < 0:
    print('No')
    exit()
left = 4 * a * b
right = (c - a - b) * (c - a - b)
if left < right:
    print('Yes')
else:
    print('No')
