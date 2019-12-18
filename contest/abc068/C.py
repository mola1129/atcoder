n, m = map(int, input().split())
transit = [False] * n
for i in range(m):
    index = float('inf')
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a == 0:
        index = b
    elif b == n - 1:
        index = a
    if index != float('inf'):
        if transit[index]:
            print('POSSIBLE')
            exit()
        else:
            transit[index] = True
print('IMPOSSIBLE')
