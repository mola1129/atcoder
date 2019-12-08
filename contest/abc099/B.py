a, b = map(int, input().split())
diff = b - a
lower = 0
for i in range(1, diff):
    lower += i
print(lower - a)
