n = int(input())
t = list(map(int, input().split()))
m = int(input())
drink = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(m):
    ans = 0
    for j in range(n):
        if drink[i][0] == j + 1:
            ans += drink[i][1]
        else:
            ans += t[j]
    print(ans)
