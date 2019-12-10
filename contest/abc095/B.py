n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]
m.sort()
x -= sum(m)
print(n + x // m[0])
