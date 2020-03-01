n = int(input())
witness = [[] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        x, y = map(int, input().split())
        witness[i].append((x - 1, y))
ans = 0
for i in range(2 ** n):
    wrong = False
    for j in range(n):
        if i >> j & 1:
            for x, y in witness[j]:
                honest = i >> x & 1
                if honest and y == 0 or not honest and y == 1:
                    wrong = True
                    break
            if wrong:
                break
        if j == n - 1:
            ans = max(ans, f.count(True))
print(ans)
