k, a, b = map(int, input().split())
if b - a <= 2 or k < a - 1:
    print(1 + k)
else:
    k -= a - 1
    times = k // 2
    print(a + (b - a) * times + k % 2)
