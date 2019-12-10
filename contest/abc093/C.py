a, b, c = map(int, input().split())
x = max(a, b, c)
total = a + b + c
if x % 2 != total % 2:
    x += 1
print((3 * x - total) // 2)
