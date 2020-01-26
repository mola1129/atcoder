n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
if k > n:
    print(0)
    exit()
total = sum(h[0: n - k])
print(total)
