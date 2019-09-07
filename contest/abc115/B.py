n = int(input())
p = [int(input()) for _ in range(n)]
p.sort()
print(p.pop(n - 1) // 2 + sum(p))
