n = int(input())
a = sorted(list(map(int, input().split())))
if n % 2 == 1 and a[0] != 0:
    print(0)
    exit()
for i in range(n % 2, n, 2):
    if a[i] != a[i + 1] or a[i] != i + 1:
        print(0)
        exit()
print(2 ** (n // 2) % (10 ** 9 + 7))
