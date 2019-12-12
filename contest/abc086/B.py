a, b = input().split()
total = a + b
total = int(total)
for i in range(1, 10001):
    if total / i == i:
        print('Yes')
        exit()
print('No')
