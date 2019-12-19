n, k = map(int, input().split())
array = [tuple(map(int, input().split())) for _ in range(n)]
array.sort()
cnt = 0
for a, b in array:
    cnt += b
    if cnt >= k:
        print(a)
        break
